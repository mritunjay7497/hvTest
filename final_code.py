#!/usr/bin/env python3

import pandas as pd
import json

# Get full data frame on terminal
# pd.set_option('display.max_rows', None) # get all rows
pd.set_option('display.max_columns', None)  # get all columns
pd.set_option('display.width', None)    # get full width

# Read the csv data and convert it to pandas dataFrame
df = pd.read_csv("data_modified_1.csv")


# Drop the duplicates entry
non_dups = df.drop_duplicates().groupby(
    ["Lab Number", "panel_code", 'Parameter Code']).agg(list)

print(non_dups)