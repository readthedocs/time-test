#!/usr/bin/python

import os
import sys
import datetime

import requests
from pyquery import PyQuery
from dateutil.parser import parse

HOST = 'https://readthedocs.com'
SLUG = 'read-the-docs-time-test'

USER = 'time-test'
PASS = 'time-test'


def login(url, session):
    # Retrieve the CSRF token first
    session.get(url)  # sets cookie
    csrftoken = session.cookies['csrftoken']

    login_data = dict(login=USER, password=PASS, csrfmiddlewaretoken=csrftoken, next='/')
    session.post(url, data=login_data, headers=dict(Referer=url))

    return session

passing = True
with open('time.rst', 'w') as time_file:
    time_file.write('Time\n====\n\n')
    time_file.write('%s' % datetime.datetime.now())
os.system('git commit -am Time && git push origin master')

with requests.Session() as session:
    login_resp = login('{host}/accounts/login/'.format(host=HOST), session)

    print("Current Time: %s " % datetime.datetime.now())
    api_resp = session.get(
        '{host}/api/v1/build/?project__slug={slug}&format=json&limit=1&type=html'.format(host=HOST, slug=SLUG),
    )

    url = '{host}/docs/{slug}/en/latest/time.html'.format(host=HOST, slug=SLUG)
    print(url)
    html_resp = session.get(url)

    five_minutes_ago = datetime.datetime.now() - datetime.timedelta(minutes=5)

    # try:
    #     # API tests
    #     obj = api_resp.json()['objects'][0]

    #     if not obj['success']:
    #         print "Build Failed"
    #         passing = False
    #     if five_minutes_ago > parse(obj['date']):
    #         print "API Build Old"
    #         passing = False
    # except:
    #     import traceback
    #     traceback.print_exc()
    #     passing = False

    # HTML tests

    pyq = PyQuery(html_resp.content)
    import ipdb; ipdb.set_trace()
    page_time = ' '.join(pyq('#time').text().split(' ')[-2:])
    print("On Page Time: %s" % page_time)
    if five_minutes_ago > parse(page_time):
        print("Time on page is Old: %s" % page_time)
        passing = False

    # Final bits
    if passing:
        print("OK")
        sys.exit(0)
    else:
        print("FAIL")
        sys.exit(2)
