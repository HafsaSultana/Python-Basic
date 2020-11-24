#HR_Inner and Outer
import numpy as np

a=np.array([int(j) for j in input().split()])

b=np.array([int(j) for j in input().split()])


print(np.inner(a,b))
print(np.outer(a,b))
