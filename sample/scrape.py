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
    ("Guam seed", 5291),
    ("Guam weed", 249),
    ("Marrentill seed", 5292),
    ("Marrentill weed", 251),
    ("Tarromin seed", 5293),
    ("Tarromin weed", 253),
    ("Harralander seed", 5294),
    ("Harralander weed", 255),
    ("Ranarr seed", 5295),
    ("Ranarr weed", 257),
    ("Toadflax seed", 5296),
    ("Toadflax weed", 2998),
    ("Irit seed", 5297),
    ("Irit weed", 259),
    ("Avantoe seed", 5298),
    ("Avantoe weed", 261),
    ("Kwuarm seed", 5299),
    ("Kwuarm weed", 263),
    ("Snapdragon seed", 5300),
    ("Snapdragon weed", 3000),
    ("Cadantine seed", 5301),
    ("Cadantine weed", 265),
    ("Lantadyme seed", 5302),
    ("Lantadyme weed", 2481),
    ("Dwarf seed", 5303),
    ("Dwarf weed", 267),
    ("Torstol seed", 5304),
    ("Torstol weed", 269)
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

