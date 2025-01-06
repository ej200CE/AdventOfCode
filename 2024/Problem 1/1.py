import numpy as np

data = np.genfromtxt("input.txt", dtype=int)

arr1 = np.sort(data[:, 0])
arr2 = np.sort(data[:, 1])

print(np.sum(abs(arr1 - arr2)))
