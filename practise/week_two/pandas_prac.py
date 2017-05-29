#!/usr/bin/env python
import pandas as pd
import numpy as np

_author_ = "rifatul.islam"

animals = ['Tiger', 'Bear', 'Moose']
# print(pd.Series(animals))
# print(np.nan == np.nan)
# print(np.isnan(np.nan))

sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
# print(pd.Series(sports))
s = pd.Series(['Tiger', 'Bear', 'Moose'], index=['India', 'America', 'Canada'])
# print(s)

sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports, index=['Golf', 'Sumo', 'Hockey'])
# print(s)

# Querying a Series

sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
sports_series = pd.Series(sports)
print(sports_series.iloc[3])
print(sports_series.loc['Golf'])
print(sports_series[3])
print(sports_series['Golf'])

int_series = pd.Series([100.00, 120.00, 101.00, 3.00])
sum = np.sum(int_series)
print(sum)

cricket_loving_countries = pd.Series(['Australia',
                                      'Barbados',
                                      'Pakistan',
                                      'England',
                                      'Bangladesh'],
                                     index=['Cricket',
                                            'Cricket',
                                            'Cricket',
                                            'Cricket',
                                            'Cricket'])
all_countries = sports_series.append(cricket_loving_countries)
print(sports_series) #Didnt changed the original list
print(all_countries)
print(all_countries.loc['Cricket'])
