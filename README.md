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

## Integrations

### Twitter

Hopelessly complicated to get the token, and I don't really remember how to do it. Not a great experience. But it works when done. Create an app and get some tokens.

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
