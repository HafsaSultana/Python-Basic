import numpy as np

n, m = map(int, input().split()) # taking number of rows and column

a = np.array([input().strip().split() for _ in range(n)], int)

m = np.mean(a, axis = 1)
v = np.var(a, axis = 0) 
s = np.std(a)

print(m)
print(v)
np.set_printoptions(legacy='1.13')
if s==0:
    print(0.0)
else:
    print("%.11f" % s)
