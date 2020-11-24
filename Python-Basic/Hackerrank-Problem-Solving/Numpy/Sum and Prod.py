# HR_Sum and Prod
import numpy as np
n, m = map(int, input().split()) # taking number of rows and column

a = np.array([input().strip().split() for _ in range(n)], int)

s =np.sum(a, axis = 0)

print(np.prod(s))


