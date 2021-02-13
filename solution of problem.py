# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 00:40:56 2021

@author: ASUS
"""
#open the file
f = open("citytemp.csv")
#read the first record and split into variables
d =f.readline()
city,temperature,unit=records.split(',')
prev = city
#position of pointer to the first record
f.seek(0)
#initialise the variables
sum=0
count=0
average=0.0
#run the loop to read all the records and do the processing
for records in f:
    records = records.rstrip('\n') #stripping the line for any new line character it may have
    city,temperature,unit=records.split(',')
    #check if the temp is in celsius then convert in degree F
    if unit=="C":
        temperature =(float(temperature) *9/5)+32
        #then again if statement to check whether the current city is equal to previous city of not
    if city!=prev:
            average=sum/count
            print(prev+" "+str(round(average,2)))
            prev=city
            sum=0
            count=0
            average=0
    sum = sum + float(temperature)
    count= count+1
    #if cities are same do the sum and calculate the average
else:
    average = sum/count()
    print(prev+" "+ str(round(average,2)))
