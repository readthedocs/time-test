#!/usr/bin/python

import os
import datetime
import time

while 1:
    with open('time.rst', 'w') as time_file:
        time_file.write('Time\n====\n\n')
        time_file.write('%s' % datetime.datetime.now())
    print datetime.datetime.now()
    os.system('git commit -am Time && git push origin master')
    time.sleep(60)


