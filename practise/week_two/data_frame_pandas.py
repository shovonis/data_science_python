#!/usr/bin/env python
import pandas as pd
import numpy as np

_author_ = "rifatul.islam"

purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

# Data Series are like rows in data frame
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store1', 'Store1', 'Store2'])
print(df)
print(df.loc['Store1', 'Name'])
print(df.loc['Store1'])  # Loc select row wise
print(df.T.loc['Name'])  # We can transpose the data frame and then select colum wise
print(df['Cost'])  # Alternative to transpose matrix
print(df.loc['Store1']['Cost'])  # Chaining query can also be done but not encouraged due to performance issue
result = df.loc[:, ['Name', 'Cost']]  # This is the most recommended way to query on multiple projection
print(result)
dropped_frame = df.drop('Store1')
print(dropped_frame)
print(df)  # The original copy doesn't change

del df['Name']
print(df)  # This deletes the column from df.

# Adding new column
df['Location'] = ['A', 'B', 'C']
print(df)
