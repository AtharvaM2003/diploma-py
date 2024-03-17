from audioop import add
from numpy import array


import numpy as np
list=[1,2,3,4,5,6,7,8,9]
arr=np.array(list)
mat1=arr.reshape(3,3)
mat2=arr.reshape(3,3)
print("Addition:\n",np.add(mat1,mat2))
print("Subtraction:\n",np.subtract(mat1,mat2))
print("Multiply:\n",np.multiply(mat1,mat2))
print("Division:\n",np.divide(mat1,mat2))
