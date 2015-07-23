#!/usr/bin/python

import os
import datetime
import time

import requests
from dateutil.parser import parse

while 1:
    with open('time.rst', 'w') as time_file:
        time_file.write('Time\n====\n\n')
        time_file.write('%s' % datetime.datetime.now())
    os.system('git commit -am Time && git push origin master')
    resp = requests.get('http://readthedocs.org/api/v1/build/?project__slug=time-test&format=json&limit=1&type=html')

    five_minutes_ago = datetime.datetime.now() - datetime.timedelta(minutes=5)
    obj = resp.json()['objects'][0]
    print "Test: %s" % str(obj['success'] == True)
    print "Test: %s" % str(parse(obj['date']) > five_minutes_ago)
    time.sleep(60)
