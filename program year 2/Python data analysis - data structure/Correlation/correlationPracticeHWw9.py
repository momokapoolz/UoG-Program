import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#read file
newDataframe = pd.read_csv('winequality-red.csv',  delimiter=';')
#print(newDataframe.to_string())


#1. DATA PROCESSING
#find the column with missing value
missing_values = newDataframe.isnull().any()

columns_with_missing_values = missing_values[missing_values].index.tolist()

print(columns_with_missing_values)
#there are no missing value here? maybe I code some line to find missing value and add them to a list but the list is empty


#2. CORRELATION
column_names = newDataframe.columns.tolist()
corre_list = []
for i in column_names:

    corre = newDataframe['fixed acidity'].corr(newDataframe[i])
    corre_list.append(corre)
    #print all correlations
    print("\n\tCorrelation between fixed acidity with ", i, ": ", corre)


#heatmap
sns.heatmap(newDataframe.corr(), annot=True, vmax=1, vmin=-1, center=0, cmap='BuPu')
plt.title("heatmap of corr")
plt.show()


#3. CORRELATION
corr_matrix = newDataframe.corr()

#max positive
def max_positive():
    corr_pairs = corr_matrix.unstack()
    sorted_pairs = corr_pairs.sort_values(kind="quicksort", ascending=False)
    highest_corr_pair = sorted_pairs[(sorted_pairs < 1)].idxmax()
    # Extract the features with the highest positive correlation
    feature_x, feature_y = highest_corr_pair

    # Create the scatter plot
    plt.scatter(newDataframe[feature_x], newDataframe[feature_y])
    plt.xlabel(feature_x)
    plt.ylabel(feature_y)
    plt.title(f'Scatter Plot of {feature_x} vs {feature_y}')
    plt.show()


#max positive
def min_positive():
    corr_pairs = corr_matrix.unstack()
    sorted_pairs = corr_pairs.sort_values(kind="quicksort", ascending=False)
    highest_corr_pair = sorted_pairs[(sorted_pairs < 1)].idxmin()
    # Extract the features with the highest positive correlation
    feature_x, feature_y = highest_corr_pair

    # Create the scatter plot
    plt.scatter(newDataframe[feature_x], newDataframe[feature_y])
    plt.xlabel(feature_x)
    plt.ylabel(feature_y)
    plt.title(f'Scatter Plot of {feature_x} vs {feature_y}')
    plt.show()


#max negative
def max_negative():
    corr_pairs = corr_matrix.unstack()
    sorted_pairs = corr_pairs.sort_values(kind="quicksort", ascending=False)
    highest_corr_pair = sorted_pairs[(sorted_pairs < 0) & (sorted_pairs >-1.0)].idxmax()
    # Extract the features with the highest positive correlation
    feature_x, feature_y = highest_corr_pair

    # Create the scatter plot
    plt.scatter(newDataframe[feature_x], newDataframe[feature_y])
    plt.xlabel(feature_x)
    plt.ylabel(feature_y)
    plt.title(f'Scatter Plot of {feature_x} vs {feature_y}')
    plt.show()


max_positive()
min_positive()
max_negative()
