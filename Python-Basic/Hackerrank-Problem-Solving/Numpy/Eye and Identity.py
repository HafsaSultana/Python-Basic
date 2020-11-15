#HR_Eye and Identity
import numpy as np

np.set_printoptions(legacy='1.13')

n, m = map(int, input().split()) # taking number of rows and column

print(np.eye(n , m , k = 0))



