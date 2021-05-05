import pandas as pd
import numpy as np
import os
from months import months_fr
'''
This script intends to process old corona cases data accumulated from 03/2020 - 05/2021
The data was orignally in single excel files from daily copy pasting'

@author: zhou
'''

# Read starter excel file
start = pd.read_excel("./Raw data/Start.xlsx")

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
# change the rest to int64 type
corona_df.iloc[:,1:] = corona_df.iloc[:,1:].apply(pd.to_numeric)

# check types
corona_df.dtypes


###################################### TESTING #################################

# Test for April 1st 2020
april1st_excel = pd.read_excel("./Raw data/2020/Corona (0.7).xlsx")


test = april1st_excel.iloc[1]
test1 = april1st_excel.iloc[[1]]
corona_df = corona_df.append(test)
corona_df = corona_df.append(test1) # both work

################################################################################

def ReadExcel (pathname):
    for file in os.listdir(pathname):
        if file.endswith('.xlsx'): 
            with pd.ExcelFile(file) as reader:
                daily = pd.read_excel(reader).T # transposed 
                
                # promote first row to column headers 
                daily.columns = daily.iloc[0]
                daily = daily[1:]

tesDir = "/Users/zhou/Desktop/Corona_test/"

corona_df.to_csv('/Users/zhou/Desktop/COMP462_A3/IR_Emission.csv', index = False, header=True)

# df = ""
# all_data = pd.DataFrame()
# for f in glob1:
#     df = pd.read_excel(f)
#     all_data = all_data.append(df,ignore_index=True)
    
# writer = pd.ExcelWriter('mycollected_data.xlsx', engine='xlsxwriter')
# all_data.to_excel(writer, sheet_name='Sheet1')
# writer.save()

#create an empty dataframe which will have all the combined data
mergedData = pd.DataFrame()
flag = 0
print((" data frame created ").center(90,'-'))
for files in os.listdir("/Users/zhou/Desktop/Corona_test/"):
    #make sure you are only reading excel files
    if files.endswith('.xlsx'):  
    #if files.endswith('.xlsx') and files.startswith('Processed'): 
        if flag == 0:
              df = pd.read_excel(files, index_col=None, usecols="A:B")
              mergedData = mergedData.append(df)
              flag = 1
        else:
             df = pd.read_excel(files, index_col=None, usecols="B:B")
             #for add empty column 
             #df['empty'] = np.nan
             # mergedData = pd.concat(mergedData, df, axis=1)
             mergedData = mergedData.append(df)
             #all_data = pd.concat(mergedData, axis=1)
             #all_data.to_excel('test.xls', index=False)
             
        print(files + " is processed.\n")
        #move the files to other folder so that it does not process multiple times
        os.rename(files, '/Users/zhou/Desktop/Corona_test/Processed/Processed '+files)
        #os.rename(files, '/Users/zhou/Desktop/Corona/'+ files[len("Processed "):len(files)])