import numpy as np

#import matplotlib.pyplot as plt

import pandas as pd

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

temp1 = np.array([5.6, 5.8, 7.9, 10.5, 13.7, 16.8, 19.1, 18.7, 15.9, 12.3, 8.4, 5.9], dtype=float)

temp2 = np.array([-8.4, -5.9, -3.4, 3.1, 8.9, 13.3, 15.3, 14.2, 9.6, 2.4, -4.7, -7.1], dtype=float)

matrix = np.array([[months], [temp1], [temp2]])

#1
print(matrix)

alter_matrix = np.transpose(matrix)

#2
print("\n")
print(alter_matrix)






