from db import insert
import requests
import re
import os
import time

base_url = "https://secure.runescape.com/m=itemdb_oldschool"

items = [
    ("ranarr_seed", "%s/Ranarr+seed/viewitem?obj=5295" % base_url),
    ("ranarr_weed", "%s/Ranarr+weed/viewitem?obj=257" % base_url)
]

for item in items:
    print("Getting requests from: %s" % item[1])
    r = requests.get(item[1])

    data = re.findall(r"average180.push\(\[new Date\('\d{4}\/\d{2}\/\d{2}'\), \d{1,10}, \d{1,10}\]\);", r.text)

    count = 0

    for average in data:
        date = re.findall(r"\d{4}\/\d{2}\/\d{2}", average)[0]
        price = int(re.findall(r"\d{1,10},", average)[0][:-1])
        trend = int(re.findall(r"\d{1,10}\]", average)[0][:-1])
        insert(item[0], date, price, trend)
        count = count + 1

    print("Inserted %d rows for: %s" % (count, item[0]))