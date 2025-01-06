import numpy as np

data = np.genfromtxt("input.txt", dtype=int)

arr1 = np.sort(data[:, 0])
arr2 = np.sort(data[:, 1])

res = abs(arr1 - arr2)
print(np.sum(res))
