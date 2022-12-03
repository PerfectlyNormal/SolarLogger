try:
    from mastodon import Mastodon
except ImportError:
    print("Importing Mastodon.py failed")

class MastodonIntegration:
    def __init__(self, mastodon_api_base, mastodon_client_key, mastodon_client_secret, mastodon_access_token):
        self._api_base = mastodon_api_base
        self._client_key = mastodon_client_key
        self._client_secret = mastodon_client_secret
        self._access_token = mastodon_access_token

    def toot(self, kWh, png_file):
        mastodon = Mastodon(
            api_base_url = self._api_base,
            client_id = self._client_key,
            client_secret = self._client_secret,
            access_token = self._access_token,
            user_agent = "GoodweSolarLogger"
        )
        status = "Today I generated "+str(kWh)+"kWh of solar electricity"
        upload = mastodon.media_post(png_file, description="A chart showing how much energy was generated per hour")
        media_ids = [upload.id]
        mastodon.status_post(status, media_ids=media_ids)