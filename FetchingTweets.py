import tweepy, os 

def fetch_tweets_from_user(user_name):
    # authentification
    auth = tweepy.OAuthHandler(os.environ['TWITTER_KEY'], os.environ['TWITTER_SECRET'])
    auth.set_access_token(os.environ['TWITTER_TOKEN'], os.environ['TWITTER_TOKEN_SECRET'])
    api = tweepy.API(auth)
    # fetch tweets
    tweets = api.user_timeline(screen_name=user, count=200, include_rts=False)
    return tweets
