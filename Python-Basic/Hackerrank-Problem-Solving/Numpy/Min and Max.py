import numpy as np
n, m = map(int, input().split()) # taking number of rows and column

a = np.array([input().strip().split() for _ in range(n)], int)

mn =np.min(a, axis = 1) 

print(np.max(mn))




