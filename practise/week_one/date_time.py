#!/usr/bin/env python
import datetime
import time

_author_ = "rifatul.islam"

print(time.time())
today = datetime.datetime.fromtimestamp(time.time())
print(today)
print(today.year, today.day, today.month)

time_delta = datetime.timedelta(days=30)

print(today-time_delta)
print(today > today - time_delta)
