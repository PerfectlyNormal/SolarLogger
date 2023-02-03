import asyncio
import datetime
import pytz
import os
import os.path

from astral import LocationInfo
from astral.sun import sun

import config
import data_handler
from plotter import Plotter

if config.mastodon_enabled:
    from integration.mastodon_integration import MastodonIntegration

timezone  = pytz.timezone(config.tz_name)
city = LocationInfo(name=config.tz_name.split('/')[1], region=config.tz_region, timezone=config.tz_name, latitude=config.latitude, longitude=config.longitude)
sun_observer = city.observer
sun_observer.elevation = config.elevation

# Set Path
path = os.path.dirname(os.path.abspath(__file__))

async def poll():
    # Sun information
    sun_info = sun(sun_observer)
    tz_info = (sun_info['sunrise']).tzinfo

    #   Time information
    now   = datetime.datetime.now()
    now   = timezone.localize(now)
    today = now.strftime("%Y-%m-%d")

    # Set the filename to be the human-readable timestamp
    csv_file = os.path.join(path, "data", today + ".csv")
    png_file = os.path.join(path, "out", today + ".png")

    suntime = datetime.datetime.now(tz_info)
    if suntime > sun_info['dawn'] and suntime < sun_info['dusk']:
        await data_handler.collect(config.IP_address, csv_file)

    if suntime > sun_info['dusk']:
        if not os.path.exists(png_file):
            kWh, x, y = data_handler.summarize(csv_file, timezone)
            Plotter(timezone, config.city_name, config.installed_max).generate_image(today, kWh, x, y, png_file)

            if config.mastodon_enabled:
                mastodon = MastodonIntegration(config.mastodon_api_base, config.mastodon_client_key, config.mastodon_client_secret, config.mastodon_access_token)
                mastodon.toot(kWh, png_file)

if __name__ == '__main__':
    asyncio.run(poll())
