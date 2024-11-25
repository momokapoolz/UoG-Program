#PRACTICE WITH MARKET.CSV FILE IN SAME DIRECTORY

#8 Columns and 28 Rows

import pandas as pd
import numpy as np
import math

#read file
newDataframe = pd.read_csv('Market.csv')

#find the column with missing value
missing_values = newDataframe.isnull().any()

columns_with_missing_values = missing_values[missing_values].index.tolist()

print(columns_with_missing_values)


#fill missing value
newDataframe['median_income'] = newDataframe['median_income'].fillna(newDataframe['median_income'].mean())
newDataframe['ocean_proximity'] = newDataframe['ocean_proximity'].fillna(newDataframe['ocean_proximity'].mode())


print(newDataframe.to_string())


#1. question
def first_ques():
    sum = 0
    count = 0
    for i in newDataframe['longitude']:
        sum += i
        count += 1

    mean_longitude = sum / count
    print("mean_longitude is: ", mean_longitude)



#2. question
def second_ques():
    std2 = newDataframe['housing_median_age'].std()
    print(std2)



#3. question 3
def third_ques():
    sum = 0
    for i in newDataframe['total_rooms']:
        sum += i

    result = sum / 4
    print(result)



#4. question 4
def four_ques():
    max = newDataframe['population'].max()
    print(max)


#5. question 5
def fifth_ques():
    min = newDataframe['median_income'].min()
    print(min)



#6.question 6
#There are 2 missing value in the given dataset, I already filled them













