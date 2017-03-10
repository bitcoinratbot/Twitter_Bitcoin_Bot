#!/usr/bin/env python
import bitcoinrpc 
from bitcoinrpc.exceptions import InsufficientFunds 
import tweepy 
from keys import keys
CONSUMER_KEY = keys['consumer_key'] 
CONSUMER_SECRET = keys['consumer_secret'] 
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret'] 

conn = bitcoinrpc.connect_to_local()
info = conn.getinfo()
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET) 
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# Creation of the actual interface, using authentication
api = tweepy.API(auth)
#Sample method used to update a status
s = api.update_status("New Block: %i" % info.blocks)
print (s)
