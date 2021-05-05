#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 20:01:47 2021

Set months names to french month names except for december 

@author: zhou
"""
import locale
import calendar


# Global vars
months_fr = []


locale.setlocale(locale.LC_ALL, 'fr_FR')
for month_idx in range(1,13):
   months_fr.append(calendar.month_name[month_idx])

# Adjust month 12 
months_fr[11] = 'decembre'


# if __name__ == "__main__":
#     print("none")