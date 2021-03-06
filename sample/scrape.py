from string import Template
from datetime import datetime
import requests
import time
import json
import db

def date(timestamp, timestamp_format = '%Y-%m-%d'):
    return datetime.utcfromtimestamp(int(timestamp)).strftime(timestamp_format)

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

    row_count = 0

    for item in items:
        request = requests.get(api_url.substitute(ITEM_ID=item[1]))
        average = json.loads(request.text)['average']
        initial_count = int(db.count_average(item[0]))

        for timestamp in average:
            day = date(timestamp[:-3])
            price = average[timestamp]
            db.insert_average(item[0], day, price)

        row_count = row_count + (int(db.count_average(item[0])) - initial_count)

    log("[%s] Inserted %d rows\n" % (date(time.time(), timestamp_format = '%Y-%m-%d %H:%M:%S'), row_count))
    time.sleep(60 * 60 * 24)

