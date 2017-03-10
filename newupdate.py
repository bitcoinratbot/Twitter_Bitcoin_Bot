#!/usr/bin/env python

## Import the modules required
import bitcoin
import bitcoin.rpc
from twython import Twython

## Create a proxy object and connect to the bitcoin.rpc
myproxy = bitcoin.rpc.Proxy()

## Get the latest CBlock data from bitcoin rpc proxy
block_info = myproxy.getblock(myproxy.getblockhash(myproxy.getblockcount()))

#Setting these as variables will make them easier for future edits
app_key =  ''
app_secret = ''
oauth_token =''
oauth_token_secret = ''

#Prepare your twitter, you will need it for everything
twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
#The above should just be a single line, without the break


a = "Bitcoin CBlock Object Info: Height "

x = myproxy.getblockcount()

P = a + str(x)

o = "Merkel Root: "

l = bitcoin.core.b2lx(block_info.hashMerkleRoot)

I = o + str(l)

twitter.update_status(status=P + "\n" + I)
 
