#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


#1.  From given data set print first and last five rows.
data = pd.read_csv("/home/vishal/Downloads/Automobile_data.csv")
print(data)
print("First five rows :\n",data.head())
print("Last five rows :\n",data.tail())


# In[7]:


#2. Clean data and update the CSV file.

data = pd.read_csv("/home/vishal/Downloads/Automobile_data.csv", na_values=({'company':("?","NA"),
                  'body-style':("?","NA"),
                  'wheel-base':("?","NA"),
                  'length':("?","NA"),
                  'engine-type':("?","NA"),
                  'num-of-cylinders':("?","NA"),
                  'horsepower':("?","NA"),
                  'average-mileage':("?","NA"),
                  'price':("?","NA")}))
print(data)
data.to_csv("Automobile_data1.csv")


# In[12]:


#3. Find the most expensive car company name.

data = pd.read_csv("Automobile_data1.csv")

data[['company','price']][data.price==data['price'].max()]


# In[21]:


#4. Print All Toyota Cars details.

data = pd.read_csv("Automobile_data1.csv")
d = data.groupby(['company'])
data = d.get_group('toyota')
data


# In[22]:


#5. Count total cars per company.

data = pd.read_csv("Automobile_data1.csv")
data['company'].value_counts()


# In[24]:


#6. Find each company’s Higesht price car.

data = pd.read_csv("Automobile_data1.csv")
d = data.groupby('company')
data = d['company','price'].max()
data


# In[25]:


#7. Find the average mileage of each car making company.

data = pd.read_csv("Automobile_data1.csv")
d = data.groupby('company')
data = d['company','price'].mean()
data


# In[28]:


#8. Sort all cars by Price column.

data = pd.read_csv("Automobile_data1.csv")
d = data.sort_values(by=['price'], ascending=False)
d


# In[33]:


#9. Concatenate two data frames using the following conditions
# Create two data frames using the following two Dicts, Concatenate those two data frames 
# and create a key for each data frame.
# GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
# japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}

GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}

dataGerman = pd.DataFrame.from_dict(GermanCars)
dataJapanes = pd.DataFrame.from_dict(japaneseCars)

data = pd.concat([dataGerman,dataJapanes], keys=["Germany","Japan"])
data


# In[35]:


#10. Merge two data frames using the following condition
# Create two data frames using the following two Dicts, Merge two data frames,
# and append the second data frame as a new column to the first data frame.
# Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
# car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}

Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}

dataCarPrice = pd.DataFrame.from_dict(Car_Price)
dataCarHorsePower = pd.DataFrame.from_dict(car_Horsepower)

data = pd.merge(dataCarPrice, dataCarHorsePower, on="Company")
data

