import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

w1lines = [52.5, 48.5, 48, 47, 45.5,54, 49.5, 45.5, 44.5, 45.5, 54.5, 43.5, 49, 41, 46.5, 53.5]
w1scores = [60, 38, 39, 51, 74, 51, 44, 36, 33, 58, 62, 33, 41, 40, 48, 60]

w2lines = [52, 41, 45, 49, 48, 47, 43, 49, 46.5, 44.5, 45, 50.5, 55, 54, 58, 56]
w2scores = [73, 59, 37, 52, 51, 35, 31, 28, 43, 33, 46, 67, 37, 66, 71, 52]

w3lines = [55.5, 43, 45.5, 46, 50, 48, 55.5, 41.5, 48, 44, 52, 41.5, 45.5, 55.5, 48.5, 51.5]
w3scores = [58, 33, 64, 32, 36, 41, 54,41, 31, 34, 50, 26, 59, 47, 58, 62]

w4lines = [49.5, 46, 47.5, 47.5, 42, 51, 42, 51.5,42.5, 44, 54, 54, 51.5, 44, 44.5, 51.5]
w4scores = [36, 45, 64, 40, 38, 64, 44, 21, 48, 51, 72, 57, 49, 30, 44, 42]

w5lines = [47.5, 54, 45.5, 50.5, 49, 39.5, 43.5, 45.5, 48.5, 39.5, 46, 46.5, 52.5, 48.5, 56.5, 46.5]
w5scores = [62, 43, 47, 47, 36, 46, 55, 39, 56, 47, 29, 89, 64, 17, 58, 56]

arr = []
for index in range(len(w4lines)):
    arr.append(w4scores[index]-w4lines[index])
    arr.append(w3scores[index]-w3lines[index])
    arr.append(w2scores[index]-w2lines[index])
    arr.append(w1scores[index]-w1lines[index])
    arr.append(w5scores[index]-w5lines[index])

fig, axs = plt.subplots()
axs.hist(arr, bins=15)
plt.show()
mean, std=norm.fit(arr)
print("MEAN", mean)
print("STD", std)
