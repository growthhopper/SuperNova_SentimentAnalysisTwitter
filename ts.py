import tweepy
from textblob import TextBlob
import csv 

api_key = 'ZAFubZisUM3WxY0zBWHVrq3Sy'
api_secret = 'oKEjaDLIbf7OXukbfTfq1D5zfJ1GXEA7m78nmNujr5mLx2aiB8'

access_token='442006100-W5dopODbBrcnJeHBiJHopRREmc5JvBTuTnt4Bfzu'
access_token_secret='EIZyBla2fzRoeX4L28DQnGSJQkVZzw3HWuTxvtGUYZnpx'

auth = tweepy.OAuthHandler(api_key, api_secret )
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('KEYWORD') # ENTER SEARCH KEYWORD HERE!

def calcPolarity(num):
    if num > 0 : 
        return "positive"
    if num < 0 :
        return "negative"
    if num == 0 :
        return "neutral"

with open('analysis.csv', mode='w') as csv_file:
    fieldnames = ['tweet', 'analysis', 'raw_analysis']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for tweet in public_tweets:
        analysis = TextBlob(tweet.text)
        writer.writerow({'tweet': tweet.text, 'analysis': calcPolarity(analysis.sentiment.polarity), 'raw_analysis' : analysis.sentiment})