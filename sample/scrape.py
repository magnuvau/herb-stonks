from string import Template
from datetime import datetime
import requests
import time
import json
import db

items = [
    ("Ranarr seed", 5295)
]

api_url = Template('https://secure.runescape.com/m=itemdb_oldschool/api/graph/${ITEM_ID}.json')

for item in items:
    request = requests.get(api_url.substitute(ITEM_ID=item[1]))
    print("API return status: %s" % request.status_code)

    daily = json.loads(request.text)['daily']
    average = json.loads(request.text)['average']
    
    for timestamp in average:
        day = datetime.utcfromtimestamp(int(timestamp[:-3])).strftime('%Y-%m-%d')
        price = average[timestamp]
        db.insert(item[0], day, price)
    
#    for timestamp in daily:
#        day = datetime.utcfromtimestamp(int(timestamp[:-3])).strftime('%d-%m-%Y')
#        price = daily[timestamp]

