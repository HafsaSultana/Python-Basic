#HR_Dot and Cross
import numpy as np

n = int(input()) # taking number of rows and column

a = np.array([input().strip().split() for _ in range(n)], int)

b = np.array([input().strip().split() for _ in range(n)], int)

print(a.dot(b))
