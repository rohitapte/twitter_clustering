import tweepy
import time
import json

# Variables that contains the user credentials to access Twitter API
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

def getFollowers(username,api):
    users = tweepy.Cursor(api.followers, screen_name=username).items()
    while True:
        try:
            user = next(users)
        except tweepy.TweepError:
            time.sleep(60*15)
            user = next(users)
        except StopIteration:
            break
        print ("@" + user.screen_name)

trends = api.trends_place(1)

search_tag="tesla"
with open("tweets_"+search_tag+'.txt','a',encoding="utf-8") as f:
    search_hashtag = tweepy.Cursor(api.search, q=search_tag+" -filter:retweets",tweet_mode='extended').items(25000)
    for tweet in search_hashtag:
        print(tweet._json)
        f.write(json.dumps(tweet._json))
        f.write("\n")
        f.flush()

