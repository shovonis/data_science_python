#!/usr/bin/env python
import datetime
import time

_author_ = "rifatul.islam"

print(time.time())
today = datetime.datetime.fromtimestamp(time.time())
print(today)
print(today.year, today.day, today.month)

time_delta = datetime.timedelta(days=30)

print(today - time_delta)
print(today > today - time_delta)

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']


def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]


# option 1
for person in people:
    print(split_title_and_name(person) == (lambda x: x.split()[0] + ' ' + x.split()[-1])(person))

# option 2
var = list(map(split_title_and_name, people)) == list(
    map(lambda person: person.split()[0] + ' ' + person.split()[-1], people))


lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

answer = [x+y+i+j for x in lowercase for y in lowercase for i in digits for j in digits]
