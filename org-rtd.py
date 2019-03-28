#!/usr/bin/python

import os
import datetime
import time
import pytz

import requests
from dateutil.parser import parse

HOST = 'https://readthedocs.org'
SLUG = 'time-test'

while 1:
    with open('time.rst', 'w') as time_file:
        time_file.write('Time\n====\n\n')
        time_file.write('%s' % datetime.datetime.now())
    os.system('git commit -am Time && git push origin master')
    URL = '{host}/api/v2/build/?project__slug={slug}&format=json&limit=1'.format(host=HOST, slug=SLUG)
    print(URL)
    resp = requests.get(URL)
    utc_time = datetime.datetime.now(tz=pytz.utc)
    five_minutes_ago = utc_time - datetime.timedelta(minutes=5)
    obj = resp.json()['results'][0]
    print("Build Test: %s" % str(obj['success'] == True))
    import ipdb; ipdb.set_trace()
    print("Time Test: %s" % str(parse(obj['date']) > five_minutes_ago))
    print("%s, %s" % (str(parse(obj['date'])), five_minutes_ago))
    time.sleep(60)
