#!/usr/bin/env python3

import pandas as pd
import json

# Get full data frame on terminal
# pd.set_option('display.max_rows', None) # get all rows
pd.set_option('display.max_columns', None)  # get all columns
pd.set_option('display.width', None)    # get full width

# Read the csv data and convert it to pandas dataFrame
df = pd.read_csv("data_modified_1.csv")


# Drop the duplicates entry and aggregate the dataframe rows in list
non_dups = df.drop_duplicates().groupby(
    ["Lab Number", "panel_code", "panel_name", "Parameter Code", "Parameter Name"]).agg(list)


# save in an excel sheet
non_dups.to_excel('output_test.xlsx')


# load the saved excel sheet
output_df = pd.read_excel('output_test.xlsx', sheet_name='Sheet1')

df = df.fillna('NaN')


def recur_dictify(frame):
    if len(frame.columns) == 7:
        if frame.values.size == 1:
            return frame.values[0][0]
        return frame.to_dict()
    grouped = frame.groupby(frame.columns[0])
    d = {k: recur_dictify(g.iloc[:, 1:]) for k, g in grouped}
    return d


required_format = recur_dictify(df.drop_duplicates())

json.dumps(required_format, ensure_ascii=False)

lab_number_list = required_format.keys()

for keys in lab_number_list:
    with open(str(keys)+'.json', 'w', encoding='utf8') as json_file:
        json.dump(required_format[keys], json_file, ensure_ascii=False)
