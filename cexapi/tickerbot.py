#!/usr/bin/python

import cexapi
import conf
import time
import json
import conf
import sys
from termcolor import colored
print(colored("Cex.io Ticker Bot", 'blue'))
def tick(col):
    try:
        col = str(col)
        api = cexapi.API(conf.username, conf.api_key, conf.api_secret)
        last = json.dumps(api.ticker('BCH/USD')['last'])
        ask = json.dumps(api.ticker('BCH/USD')['ask'])
        bid = json.dumps(api.ticker('BCH/USD')['bid'])
        print(colored("Last: %s Ask: %s Bid %s " % (last, ask, bid), col))
    except Exception as err:
        print("Error: %s" % err)
        pass

while True:
    try:
        tick('red')
        time.sleep(1)
        tick('green')
        time.sleep(1)
    except KeyboardInterrupt:
        sys.exit(0)
