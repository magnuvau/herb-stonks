from db import insert
import requests
import re
import os
import time

url = "https://secure.runescape.com/m=itemdb_oldschool/Ranarr+seed/viewitem?obj=5295"

print("Fetching ranarr seed...", end="")
r = requests.get(url)
print(r.status_code)

data = re.findall(r"average180.push\(\[new Date\('\d{4}\/\d{2}\/\d{2}'\), \d{1,10}, \d{1,10}\]\);", r.text)

print("Inserting data...", end="")
for average in data:
    date = re.findall(r"\d{4}\/\d{2}\/\d{2}", average)[0]
    price = int(re.findall(r"\d{1,10},", average)[0][:-1])
    trend = int(re.findall(r"\d{1,10}\]", average)[0][:-1])
    insert('ranarr', date, price, trend)

print("Done!")
