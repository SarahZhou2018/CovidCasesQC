import pandas as pd
import numpy as np
import os
import processing_module
import timing

'''
This script intends to process old corona cases data accumulated from 03/2020 - 05/2021
The data was orignally in single excel files from daily copy pasting'

@author: zhou
'''

##################### Processing starter Excel file ###########################

# Read starter excel file
start = pd.read_excel("../raw data/Start.xlsx")

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
april1st_excel = pd.read_excel("../raw data/2020/Corona (0.7).xlsx")
april1st_excel = april1st_excel.T

daily_values = april1st_excel.iloc[1]

# Test2 for April 19th 2020, length of values: 21
april1st_excel = pd.read_excel("../raw data/2020/Corona (16).xlsx")
april1st_excel = april1st_excel.T

daily_values = april1st_excel.iloc[1]

# Arguments
path = "../raw data/2020/Corona (16).xlsx"
s = daily_values.name
################################################################################


# 1 - Process date 
# 2 - Process values
# values = processing_module.process_daily_values(daily_values)
# date = processing_module.process_date(s, path)

# values.insert(0, date)
# new_row = pd.Series(values, index = corona_df.columns)
# corona_df = corona_df.append(new_row, ignore_index = True)


################################################################################

def process_excel_files(directory):
    
    global corona_df
    
    for filename in os.listdir(directory):
        
        if filename.endswith('.xlsx'): 
            
            pathname = os.path.join(directory, filename)
            
            print("processing" + pathname)
            
            daily = pd.read_excel(pathname).T # transposed 
            
            daily_values = daily.iloc[1]
            
            s = daily_values.name

            # 1 - Process date 
            date = processing_module.process_date(s, pathname)
            # 2 - Process values
            values = processing_module.process_daily_values(daily_values)
            
            # Create new row
            values.insert(0, date)
            new_row = pd.Series(values, index = corona_df.columns)
            corona_df = corona_df.append(new_row, ignore_index = True)

    
    return


process_excel_files("../raw data/2020/")
process_excel_files("../raw data/2021/")
corona_df = corona_df.sort_values(by='Date')
corona_df.drop_duplicates( inplace = True)


# check sum of columns = to Total column






timing.endlog()






