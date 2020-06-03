import numpy as np


# In[9]:


#1. Write a NumPy program to get the numpy version and show numpy build configuration.
print(np.__version__)
print(np.show_config())


# In[16]:


#2. Write a NumPy program to test element-wise for complex number, real number of a given array. 
# Also test whether a given number is a scalar type or not.

arr = np.array([1+1j, 1+2j, 3.5, 7])
print(np.iscomplex(arr))
print(np.isreal(arr))
print(np.isscalar(arr))


# In[18]:


#3. Write a NumPy program to test whether none of the elements of a given array is zero.

arr = np.array([1,2,3,0,1,5,6])
print(np.all(arr))


# In[24]:


#4. Write a NumPy program to test whether any of the elements of a given array is non-zero.

arr = np.array([0,1,0])
print(np.any(arr))
#o/p = True
arr = np.array([0,0,0])
print(np.any(arr))


# In[29]:


#5. Write a NumPy program to test element-wise for NaN of a given array.

arr = np.array([1,2,np.NaN,4])
print(np.isnan(arr))

arr = np.array([1,2,3,4])
print(np.isnan(arr))


# In[30]:


#6. Write a NumPy program to create an element-wise comparison (greater, greater_equal, less and 
# less_equal) of two given arrays.

arr1 = np.array([1,2,3,4,5,6])
arr2 = np.array([2,3,4,1,5,3])
print(arr1 > arr2)
print(arr1 >= arr2)
print(arr1 < arr2)
print(arr1 <= arr2)


# In[33]:


#7. Write a NumPy program to create an element-wise comparison 
# (equal, equal within a tolerance) of two given arrays.

arr1 = np.array ([72, 79, 85, 90, 150, -135, 120, -10, 60, 100])
arr2 = np.array ([72, 79, 85, 90, 150, -135, 120, -10, 60, 100.000001])
print("Equality check : ",arr1 == arr2)
print("Tolerance : ",np.allclose(arr1,arr2))


# In[34]:


#8. Write a NumPy program to create an array with the values 1, 7, 13, 105 and 
# determine the size of the memory occupied by the array.

arr = np.array([1,7,13,105])
print("Size of the memory : ",arr.itemsize*arr.size)


# In[36]:


#9. Write a NumPy program to create an array of 10 zeros, 10 ones, 10 fives.

arrZeroes = np.zeros(10)
print("Zeroes : ", arrZeroes)
arrOnes = np.ones(10)
print("Ones : ", arrOnes)
arrFive = np.ones(10)*5
print("Fives : ", arrFive)


# In[38]:


#10. Write a NumPy program to create an array of the integers from 30 to 70.

arr = np.arange(30,71)
print("Array is : ", arr)


# In[39]:


#11. Write a NumPy program to create an array of all the even integers from 30 to 70.

arr = np.arange(30,71, 2)
print("Even Array is : ", arr)


# In[41]:


#12. Write a NumPy program to create a 3x3 identity matrix.

arr = np.arange(10,19).reshape(3,3)
print("3 * 3  matrix is : \n", arr)


# In[53]:


#13. Write a NumPy program to generate a random number between 0 and 1.

ran = np.random.random(1)
print("Random num 0 and 1 is : ", ran)


# In[56]:


#14. Write a NumPy program to generate an array of 15 random numbers from a standard normal distribution.

ranNum = np.random.normal(1,15,15)
print("Random num 0 and 1 is : ", ranNum)


# In[58]:


#15. Write a NumPy program to create a vector with values ranging from 15 to 55 and print all values 
# except the first and last.

arrVec = np.arange(15,56)
print("except first and last value :\n",arrVec[1:-1])

