import numpy

def arrays(arr):
    b = numpy.array(arr[::-1] ,float) # (This line is my code)
    return b

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
