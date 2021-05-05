import pandas as pd
import numpy as np
import os
import processing_module

'''
This script intends to process old corona cases data accumulated from 03/2020 - 05/2021
The data was orignally in single excel files from daily copy pasting'

@author: zhou
'''

##################### Processing starter Excel file ###########################

# Read starter excel file
start = pd.read_excel("../Raw data/Start.xlsx")

# Initialize a dataframe
corona_df= start.T

# promote first row to column headers 
corona_df.columns = corona_df.iloc[0].tolist()
corona_df = corona_df[1:]

# promote indices to the Date column
corona_df.index.name = 'Date'
corona_df.reset_index(level=0, inplace=True)


# change to date type
corona_df['Date'] = pd.to_datetime(corona_df.Date)
# change the rest to type int64 
corona_df.iloc[:,1:] = corona_df.iloc[:,1:].apply(pd.to_numeric)

# check types
corona_df.dtypes


###################################### TESTING #################################


# Test1 for April 1st 2020, length of values: 19
april1st_excel = pd.read_excel("../Raw data/2020/Corona (0.7).xlsx")
april1st_excel = april1st_excel.T

daily_values = april1st_excel.iloc[1]

# Test2 for April 19th 2020, length of values: 21
april1st_excel = pd.read_excel("../Raw data/2020/Corona (16).xlsx")
april1st_excel = april1st_excel.T

daily_values = april1st_excel.iloc[1]

# Arguments
path = "../Raw data/2020/Corona (16).xlsx"
s = daily_values.name
################################################################################


# 1 - Process date 
# 2 - Process values
values = processing_module.process_daily_values(daily_values)
date = processing_module.process_date(s, path)

values.insert(0, date)
new_row = pd.Series(values, index = corona_df.columns)
corona_df = corona_df.append(new_row, ignore_index = True)

# import glob
# glob1 = glob.glob("/Users/zhou/Desktop/Coronatest/*.xlsx")

################################################################################
def ReadExcel (pathname):
    for file in os.listdir(pathname):
        if file.endswith('.xlsx'): 
            with pd.ExcelFile(file) as reader:
                daily = pd.read_excel(reader).T # transposed 
                
                # promote first row to column headers 
                daily.columns = daily.iloc[0]
                daily = daily[1:]

