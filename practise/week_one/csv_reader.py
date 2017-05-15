#!/usr/bin/env python
import csv

_author_ = "rifatul.islam"

with open("mpg.csv") as csv_file:
    mpg = list(csv.DictReader(csv_file))

print(mpg[:10])
print(len(mpg))
print(mpg[0].keys())
print(sum(float(d['weight']) for d in mpg) / len(mpg))

# Avg mpg per cylinder

cyl = set(d['cylinders'] for d in mpg)
print(cyl)
avg_mpg_cyl = []

for c in cyl:
    sum_mpg = 0
    total_mpg = 0
    for d in mpg:
        if d['cylinders'] == c:
            sum_mpg += float(d['mpg'])
            total_mpg += 1

    avg_mpg_cyl.append((c, sum_mpg / total_mpg))

avg_mpg_cyl.sort(key=lambda x: x[0])
print(avg_mpg_cyl)

# Average acceleration per origin class
origin_class = set(d['origin'] for d in mpg)
acceleration = []

for oc in origin_class:
    sum_hp = 0
    counter = 0
    for d in mpg:
        if oc == d['origin']:
            sum_hp += float(d['acceleration'])
            counter += 1

    acceleration.append((oc, sum_hp / counter))

acceleration.sort(key=lambda x: x[0])

print("Avg acceleration: ", acceleration)
