#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 20:01:47 2021

@author: zhou
"""
import locale
import calendar
import re 
import datetime
import pandas as pd
import numpy as np


# Global vars
# french months names except for december 
months_fr = []

locale.setlocale(locale.LC_ALL, 'fr_FR')
for month_idx in range(1,13):
   months_fr.append(calendar.month_name[month_idx])

# Adjust month 12 
months_fr[11] = 'decembre'



# 1 - Process date 
'''
Takes a string as argument
'''
def process_date(s, path): 
    day = ""
    month = 0
    year = 0
    
    # 1- find day
    for i, c in enumerate(s):
        if c.isdigit():
            day += c
            if s[i+1].isdigit():
                day += s[i+1]
            
            break
        
    day = int(day)  
    
    # Error handling    
    if day == 0 or day > 32:
        raise Exception('The day of the month found is'+ day )
    
    
    # 2- find month
    for word in months_fr:
        if word in s:
            month = months_fr.index(word) + 1
            
    # Error handling    
    if month == 0 or month > 12:
        raise Exception('The month found is'+ month) 
           
        
    # 3- find year
    match = re.search(r'2020', path)
    if match:
        print ('found', match.group())
        year = 2020
    else:
        print ('did not find 2020')
        year = 2021
    

    return datetime.datetime(year, month, day)




# 2 - Process daily case counts
'''
Takes a pandas.Series as argument
'''
def process_daily_values(daily_values):
    if (len(daily_values) < 21):
        
        # determine the numer of seros to pad because of different lengths 
        num_zeros = 21 - len(daily_values)
        # index of insertion 
        index = len(daily_values) - 2
        # insert zeros 
        daily_values = pd.Series(np.insert(
            daily_values.values, index+1, values=[0]*num_zeros, axis=0
            ))
        
        
    # remove white spaces
    daily_values = daily_values.replace(' ', '', regex=True)
    
    # change to type int64
    daily_values = pd.to_numeric(daily_values).tolist()
    # daily_values = pd.Series.astype(daily_values, 'int64')
    
    return daily_values



# if __name__ == "__main__":
#     print("none")