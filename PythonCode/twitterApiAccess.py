# To run this code, first edit config.py with your configuration, then:
#
# mkdir data
# python twitter_stream_download.py -q apple -d data
# 
# It will produce the list of tweets for the query "apple" 
# in the file data/stream_apple.json

import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import argparse
import string
import config
import json
import sys
import elasticsearch
from textwrap import TextWrapper
from datetime import datetime
from elasticsearch import Elasticsearch

es = elasticsearch.Elasticsearch()
auth = OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_secret)
api = tweepy.API(auth)

def get_parser():
    """Get parser for command line arguments."""
    parser = argparse.ArgumentParser(description="Twitter Stream Downloader")
    parser.add_argument("-q",
                        "--query",
                        dest="query",
                        help="Query/Filter",
                        default='-')
    return parser

class TwitterListener(tweepy.StreamListener):
    status_wrapper = TextWrapper(width=60, initial_indent='    ', subsequent_indent='    ')

    def on_status(self, status):
        try:
            json_data = status._json

            es.create(index="twitter",
                doc_type="tweet",
                body=json_data)

        except Exception, e:
            print e
            pass

streamer = tweepy.Stream(auth=auth, listener=TwitterListener(), timeout=3000000000)

parser = get_parser()
args = parser.parse_args()
print(args.query)
terms = ['bernie','feelthebern']
streamer.filter(None,terms)