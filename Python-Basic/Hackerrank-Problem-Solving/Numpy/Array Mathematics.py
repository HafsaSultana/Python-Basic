import numpy as np
n, m = map(int, input().split()) # taking number of rows and column

a = np.array([input().strip().split() for _ in range(n)], int)

b = np.array([input().strip().split() for _ in range(n)], int)

print(a + b)
print(a - b)
print(a * b)
print(a//b)
print(a%b)
print(a**b)
