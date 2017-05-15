#!/usr/bin/env python
import csv

_author_ = "rifatul.islam"

with open("mpg.csv") as csv_file:
    mpg = list(csv.DictReader(csv_file))

print(mpg[:3])
print(len(mpg))
print(mpg[0].keys())
print(sum(float(d['weight']) for d in mpg) / len(mpg))

cyl = set(d['cylinders'] for d in mpg)
print(cyl)


# Avg mpg per cylinder
avg_mpg_cyl = []
for c in cyl:
    sum_mpg = 0
    total_mpg = 0
    for d in mpg:
        if d['cylinders'] == c:
            sum_mpg += float(d['mpg'])
            total_mpg += 1

    avg_mpg_cyl.append((c, sum_mpg/total_mpg))

avg_mpg_cyl.sort(key=lambda x: x[0])
print(avg_mpg_cyl)

