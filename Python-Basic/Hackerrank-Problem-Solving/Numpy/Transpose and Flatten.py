import numpy as np
n, m = map(int, input().split()) # taking number of rows and column

arr = np.array([input().strip().split() for _ in range(n)], int)

print(np.transpose(arr))
print(arr.flatten())
