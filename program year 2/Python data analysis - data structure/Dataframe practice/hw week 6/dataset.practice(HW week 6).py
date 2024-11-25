import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as c

newDataframe = pd.read_csv('winequality-red.csv', delimiter=';')

#1: 3 rows head and 2 rows bottom
first_3_rows = newDataframe.head(3)
last_2_rows = newDataframe.tail(2)


# highest density row
sorted_by_density = newDataframe.sort_values(by='density', ascending=False)
highest_density_rows = sorted_by_density.head(5)


#2: create a new dataset from rows
# volatile_acidity = newDataframe['volatile acidity']
# free_sulfur_dioxide = newDataframe['free sulfur dioxide']
# total_sulfur_dioxide = newDataframe['total sulfur dioxide']
# pH = newDataframe['pH']
# alcohol = newDataframe['alcohol']

#here is the new dataset
new_dataset = pd.DataFrame({
    'volatile_acidity': newDataframe['volatile acidity'],
    'free_sulfur_dioxide': newDataframe['free sulfur dioxide'],
    'total_sulfur_dioxide': newDataframe['total sulfur dioxide'],
    'pH': newDataframe['pH'],
    'alcohol': newDataframe['alcohol']
})

#save to csv file
new_dataset.to_csv('daya6_redWine_dataset.csv')


#3 heatmap
data = new_dataset.to_numpy()

colors_list = ['#009900', '#00cc00']
cmap = c.ListedColormap(colors_list)

plt.imshow(data, cmap=cmap, vmin=0, vmax=100, extent=[0, 10, 0, 10])
for i in range(10):
    for j in range(10):
        plt.annotate(str(data[i][j]), xy=(j+0.5, i+0.5),
                     ha='center', va='center', color='white')

cbar = plt.colorbar()#ticks=[0, 5, 100])
cbar.ax.set_yticklabels(['Very Low','Low', 'Low Medium', 'Medium', 'High', 'Very High'])

plt.title( "A Heat Map in simplest form-5" )
plt.show()




