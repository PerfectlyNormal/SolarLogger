# GoodWe Solar Logger

Log the performance of your solar panels with a GoodWe inverter.

This will create a .csv file with a timestamp, the real-time power being generated (Watts), and total energy generated that day (kWh).

The script attempts to read from the inverter every time it runs. The first time it runs after the sun is down, it generates a PNG and optionally shares it using one of the integrations.

You can place this in your crontab to run every minute - or as often as you wish.

Example crontab:

```bash
* * * * * cd /home/solar/app && ./venv solar.py
```

## Configuration

Copy `config.sample.py` to `config.py` and update the configuration.

`IP_address` is the IP address of your inverter.

`installed_max` is the maximum production in Watts, and used for scaling the generated graph.

`city_name` gets printed in the header of the graph, but no validation is done, so can be anything.

`tz_name`/`tz_region`, `latitude`/`longitude` and `elevation` is used for determining when the sun is up or not.

## Data format

Each run attempts to connect to the inverter and report back. Since the inverter gets its power from the sun, it's not always online.
Nothing gets written when it does not respond, so each csv-file may have gaps at the beginning and end of the day.

The result gets written to a CSV file with two columns:

1. the timestamp in UTC
2. the current power in watts

## Integrations

### Twitter

(╯°□°）╯︵ ┻━┻

### Mastodon

Live example: [@PerfectlyNormalSolar@botsin.space](https://botsin.space/@PerfectlyNormalSolar)

Set up your own:

1. Create an account for your bot on a chosen server
2. Create an application under Preferences -> Development
    * Give the application a nice name
    * Leave the redirect URI
    * Needs at least `write:media` and `write:statuses` scopes in order to work
3. Copy the client key/secret and access token into `config.py`
4. Set `mastodon_enabled` to `True` and wait for it to work.

## Credits

Based on a copy of [@edent](https://github.com/edent/)'s [Fronius-DataManager-Solar-Logger](https://github.com/edent/Fronius-DataManager-Solar-Logger).
