import configure, os, tweepy, argparse

def getTweet(name, tweet_id, numberOfReplies):
    replies=[]
    for tweet in tweepy.Cursor(api.search,q='to:'+name, result_type='recent', timeout=999999).items(numberOfReplies):
        if hasattr(tweet, 'in_reply_to_status_id_str'):
            if (tweet.in_reply_to_status_id_str==tweet_id):
                replies.append(tweet)
    return replies

if __name__ == '__main__': 
    parser = argparse.ArgumentParser(description='Access all replies to a specific tweet')
    parser.add_argument('--n', '--name', required= True, help='name of the account whose post is to be tracked')
    parser.add_argument('--id', '--tweet_id', default='', help='the id of the tweet to be tracked')
    parser.add_argument('--n', '--numberOfReplies', default=10, help='the number of replies to produce')
    name, tweet_id, numberOfReplies = list(vars(parser.parse_args()).values())
    configured = configure()
    if configured:
        CONSUMER_KEY = os.getenv("CONSUMER_KEY")
        CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
        ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
        ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
        # Authentication with Twitter
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        tweetAPI = tweepy.API(auth)
        replies = getTweet(name, tweet_id, numberOfReplies)
        print(replies)