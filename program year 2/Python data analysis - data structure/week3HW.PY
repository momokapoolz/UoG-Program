import matplotlib.pyplot as plt
import numpy as np

cheo_len1 = np.array([0, 10])
cheo_len2 = np.array([0, 10])

cheo_xuong1 = np.array([0, 10])
cheo_xuong2 = np.array([10, 0])

ngang1 = np.array([0, 10])
ngang2 = np.array([5, 5])

doc1 = np.array([5, 5])
doc2 = np.array([0, 10])

plt.plot(cheo_len1, cheo_len2)
plt.plot(cheo_xuong1, cheo_xuong2)
plt.plot(ngang1, ngang2)
plt.plot(doc1, doc2)
plt.show()
