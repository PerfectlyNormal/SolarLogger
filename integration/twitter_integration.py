try:
    import tweepy
except ImportError:
    print("Importing tweepy failed")

class TwitterIntegration:
    def __init__(self, twitter_bearer_token, twitter_consumer_key, twitter_consumer_secret, twitter_access_token, twitter_access_token_secret) -> None:
        self._bearer_token = twitter_bearer_token
        self._consumer_key = twitter_consumer_key
        self._consumer_secret = twitter_consumer_secret
        self._access_token = twitter_access_token
        self._access_token_secret = twitter_access_token_secret
        
    def tweet_image(self, kWh, png_file):
        auth = tweepy.OAuthHandler(self._consumer_key, self._consumer_secret)
        auth.set_access_token(self._access_token, self._access_token_secret)

        # Creation of the actual interface, using authentication
        twitter_api = tweepy.API(auth)
        status = "Today I generated "+str(kWh)+"kWh of solar electricity"
        upload = twitter_api.media_upload(png_file)
        media_ids = [upload.media_id_string]
        twitter_api.update_status(status=status, media_ids=media_ids)
