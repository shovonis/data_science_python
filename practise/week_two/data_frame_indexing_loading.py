#!/usr/bin/env python
import pandas as pd

_author_ = "rifatul.islam"

df = pd.read_csv("olympics.csv", index_col=0, skiprows=1)
# print(df.head())

# print(df.columns)

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

# print(df.head())

# Boolean masking
# print(df["Gold"] > 0)
only_gold = df.where(df['Gold'] > 0)
only_silver = df.where(df['Silver'] > 0).dropna()
# print(only_silver['Silver'].count())
only_bronze = df[df['Bronze'] > 0]  # Alternate way of the where query
# print(only_bronze['Bronze'].count())

# print(only_gold['Gold'].count())
# print(df['Gold'].count())
only_gold = only_gold.dropna()
# print(only_gold.head())

only_gold = df[df['Gold'] > 0]
# print(only_gold.head())
# print(len(df[(df["Gold"] > 0) | (df['Gold.1'])]))
# print(df.index)

# print(len(df[(df['Gold'] > 0) & (df['Gold'] < 2)]))

df['Country'] = df.index
df.set_index('Gold', inplace=True)
# print(df.head())
df.reset_index()
# print(df.head())

df = pd.read_csv('census.csv')
# print(df.head())
# print(df.count())
# print(df['SUMLEV'].unique())
# df = df[df['SUMLEV'] == 50]
# print(df.head())

columns_to_keep = ['STNAME',
                   'CTYNAME',
                   'BIRTHS2010',
                   'BIRTHS2011',
                   'BIRTHS2012',
                   'BIRTHS2013',
                   'BIRTHS2014',
                   'BIRTHS2015',
                   'POPESTIMATE2010',
                   'POPESTIMATE2011',
                   'POPESTIMATE2012',
                   'POPESTIMATE2013',
                   'POPESTIMATE2014',
                   'POPESTIMATE2015']

df = df[columns_to_keep]

# Multiple Indexing

df.set_index(['STNAME', 'CTYNAME'], inplace=True)
# print(df.head())

# Printing first and second indexwise
# print(df.loc['Alabama', 'Bibb County'])

print(df.loc[[('Alabama', 'Bibb County'),
              ('Michigan', 'Wayne County')]])


