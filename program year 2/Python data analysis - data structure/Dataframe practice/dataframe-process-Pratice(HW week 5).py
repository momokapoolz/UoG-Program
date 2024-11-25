import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#1
newDataframe = pd.read_csv('winequality-red.csv', delimiter=';')
print(newDataframe.to_string())

dimensions = newDataframe.shape
print(f"The dimensions of the dataset are: {dimensions[0]} rows and {dimensions[1]} columns.")



#2
def std_of_volcatile():
    std2 = newDataframe['volatile acidity'].std()
    print(std2)

def mean_of_chlorides():
    sum = 0
    count = 0
    for i in newDataframe['chlorides']:
        sum += i
        count += 1

    mean_chlorides = sum / count
    print("mean_chlorides is: ", mean_chlorides)

def max_pH():
    max = newDataframe['pH'].max()
    print(max)

def min_sulphates():
    min = newDataframe['sulphates'].max()
    print(min)

def half_density():
    sum = 0
    for i in newDataframe['density']:
        sum += i

    result = sum / 2
    print(result)


#3
def count_alcohol_morethan10():
    count = 0
    for i in newDataframe['alcohol']:
        if(i > 10):
            count += 1
    print(count)

count_alcohol_morethan10()


#4
def find_best_quality_wine():
    max = newDataframe['quality'].max()
    print(max)

def cound_worst_quality_wine():
    min = newDataframe['quality'].min()
    count = 0
    for i in newDataframe['quality']:
        if i == min:
            count += 1
    print(count)


#5
def find_and_count_highest_density():
    max = newDataframe['density'].max()
    print(max)
    count = 0
    for i in newDataframe['density']:
        if i == max:
            count += 1
    print(count)


#6
def count_wine_less_than_2point5_residual_sugar():
    count = 0
    for i in newDataframe['residual sugar']:
        if i < 2.5:
            count += 1
    print(count)

#7
def visualize_chart():
    column_array = newDataframe['quality'].to_numpy()

    plt.figure(figsize=(10, 5))
    sns.boxplot(y=column_array)
    plt.title('Box Plot Chart')
    plt.show()

visualize_chart()