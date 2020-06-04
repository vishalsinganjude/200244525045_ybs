#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[7]:


#1. Write a NumPy program to create a 3X4 array using range and iterate over it.

arr = np.arange(40,52).reshape(3,4)
print("3 * 4 matrix is :\n",arr)
print("After Iterate : ")
for i in np.nditer(arr):
    print(i,end="  ")


# In[5]:


#2. Write a NumPy program to create a vector of length 10 with values evenly distributed between 5 and 50.

arr = np.arange(5,51,5)
print("array of length 10 is :\n",arr)


# In[9]:


#3. Write a NumPy program to create a vector with values from 0 to 20 and change the sign of 
# the numbers in the range from 9 to 15. 

arr = np.arange(0,21)
print("Original Vector :\n",arr)
arr[(arr>8) & (arr < 16)] *= -1
print("after Changes the signs :\n", arr)


# In[10]:


#4. Write a NumPy program to create a vector of length 5 filled with arbitrary integers from 0 to 10.

arr = np.random.randint(0,11,5)
print("Arbitrary Integers are :\n", arr)


# In[12]:


#5. Write a NumPy program to multiply the values of two given vectors.

arr1 = np.arange(1,5)
arr2 = np.arange(5,9)
arr3 = arr1 * arr2
print("After Multiplication of two vectors :\n", arr3)


# In[15]:


#6. Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.

arr = np.arange(10, 22).reshape(3,4)
print("3 * 4 matrix with 10 to 21 values :\n",arr)


# In[16]:


#7. Write a NumPy program to find the number of rows and columns of a given matrix.

arr = np.arange(10, 22).reshape(3,4)
print("rows and columns are : ",np.shape(arr))


# In[19]:


#8. Write a NumPy program to create a 3x3 identity matrix, i.e. diagonal elements are 1, the rest are 0.

arr = np.eye(3)
print("Diagonal elements are : \n",arr)


# In[20]:


#9. Write a NumPy program to create a 10x10 matrix, in which the elements on the borders will be equal to 1,
# and inside 0.

arr = np.ones((10,10))
arr[1:-1, 1:-1] = 0
print("The borders elements 1 and inside 0 :\n", arr)


# In[21]:


#10. Write a NumPy program to create a 5x5 zero matrix with elements on the main diagonal equal to 1, 2, 3, 4, 5.

arr = np.diag([1,2,3,4,5])
print("5 x 5 zero matrix with diagonal :\n",arr)


# In[22]:


#11. Write a NumPy program to create a 4x4 matrix in which 0 and 1 are staggered, with zeros on the main diagonal.

arr = np.zeros((4,4))
arr[::2,1:2] = 1
arr[1:2,::2] = 1
print("Create 4x4 matrix in 0 and 1 and zeroes in diagonal :\n", arr)


# In[24]:


#12. Write a NumPy program to create a 3x3x3 array filled with arbitrary values.

arr = np.random.randint(((3,3,3)))
print("Random 3x3x3 array :\n", arr)


# In[27]:


#13. Write a NumPy program to compute sum of all elements, sum of each column and sum of each row of a given array.

arr = np.array([[2,3],[5,4]])
print("array :\n",arr)
print("Sum of array : ", np.sum(arr))
print("Sum of axis 0 array : ", np.sum(arr, axis=0))
print("Sum of axis 1 array : ", np.sum(arr, axis=1))


# In[28]:


#14. Write a NumPy program to compute the inner product of two given vectors.

arr1 = np.array([5,6])
arr2 = np.array([2,3])
print("The Inner Product of two given vectors :\n",np.dot(arr1, arr2))


# In[30]:


#15. Write a NumPy program to add a vector to each row of a given matrix

arr = np.arange(1,10).reshape(3,3)
print("3 * 3 vector :\n", arr)
print("sum of vectors row wise :\n", np.sum(arr, axis=0))

