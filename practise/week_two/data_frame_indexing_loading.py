#!/usr/bin/env python
import pandas as pd

_author_ = "rifatul.islam"

df = pd.read_csv("olympics.csv", index_col=0, skiprows=1)
print(df.head())

print(df.columns)

# Renaming the column
for col in df.columns:
    if col[:2] == '01':
        df.rename(columns={col: 'Gold' + col[4:]}, inplace=True)
    if col[:2] == '02':
        df.rename(columns={col: 'Silver' + col[4:]}, inplace=True)
    if col[:2] == '03':
        df.rename(columns={col: 'Bronze' + col[4:]}, inplace=True)
    if col[:2] == 'No':
        df.rename(columns={col: '#' + col[2:]}, inplace=True)
    if col[:1] == '№':
        df.rename(columns={col: '#' + col[1:]}, inplace=True)

print(df.head())

