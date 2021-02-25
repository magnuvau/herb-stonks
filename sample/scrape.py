from string import Template
from datetime import datetime
import requests
import time
import json
import db

def date(timestamp):
    return datetime.utcfromtimestamp(int(timestamp)).strftime('%Y-%m-%d')

def log(msg):
    with open('scrape.log', 'a') as log:
        log.write(msg)
        log.close()

items = [
    ("Ranarr seed", 5295),
    ("Ranarr weed", 257)
]

api_url = Template('https://secure.runescape.com/m=itemdb_oldschool/api/graph/${ITEM_ID}.json')

while(True):

    for item in items:
        request = requests.get(api_url.substitute(ITEM_ID=item[1]))
        average = json.loads(request.text)['average']
      
    for timestamp in average:
      day = date(timestamp[:-3])
      price = average[timestamp]
      db.insert_average(item[0], day, price)

    log("[%s] Scraped!\n" % date(time.time()))
    time.sleep(60 * 60 * 24)

