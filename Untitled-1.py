import numpy as np
from numpy import arange

list = [1, 2, 3, 4, 5]
print(list)

array = np.array(list)
print(array)

print(list*2)
print(array*2)

list.append(2)  # array.append(2) --> not possible! It's fixed size!
print("list", list)
# 1D arrays
print(np.arange(10))
print(np.zeros(10))
print(np.ones(10))
print("random randint", np.random.randint(-5, 6, 10))  # start:stop:step
print("random randint", np.random.randint(-5, 6, 10))
print("random.random * 2", np.random.random(10)*2)
print("random.random", np.random.random(10))

# 2D arrays
print(np.zeros((4, 3)))
print(np.full((2, 10), 7))
print(np.random.randint(-10, 10, (2, 4, 3)))


# Reshaping & converting an array
array = np.random.randint(-5, 6, 10)
print(array)
print("array is of type:", array.dtype)
array_float = array.astype('f')
print(array_float)
array_2D = np.reshape(array, (2, 5))
print(array_2D)

numbers = [6, 8, 6, 7, 6, 1, 8, 2, 0, 5]
array = np.array(numbers)
print(array)
print(array[1:5:1])
print(array[1:5:2])  # start[index]:stop[index](ex):step
print
