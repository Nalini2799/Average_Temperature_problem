# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 00:36:47 2021

@author: ASUS
"""
#open the file
f = open('citytemp.csv','a+')
f = open('citytemp.csv','r+')
#read file
t = f.readline()
y = f.readlines()
#data processing
city, temperature , unit = t.split(',')
temperature =(int(temperature) - 32) * 5/9
#write records to file
f.write(t)

f.seek(0) #shifting pointer to the initial
for records in f:
    records = records.rstrip('\n') #deleting extra space 
    print(records)
