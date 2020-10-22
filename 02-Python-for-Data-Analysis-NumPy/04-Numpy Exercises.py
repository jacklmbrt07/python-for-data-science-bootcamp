#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___

# # NumPy Exercises 
# 
# Now that we've learned about NumPy let's test your knowledge. We'll start off with a few simple tasks, and then you'll be asked some more complicated questions.

# #### Import NumPy as np

# In[1]:


import numpy as np


# #### Create an array of 10 zeros 

# In[5]:


np.zeros(10)


# #### Create an array of 10 ones

# In[6]:


np.ones(10)


# #### Create an array of 10 fives

# In[7]:


np.ones(10)*5


# #### Create an array of the integers from 10 to 50

# In[10]:


np.arange(10, 51)


# #### Create an array of all the even integers from 10 to 50

# In[11]:


np.arange(10, 51, 2)


# #### Create a 3x3 matrix with values ranging from 0 to 8

# In[13]:


np.arange(0,9).reshape(3,3)


# #### Create a 3x3 identity matrix

# In[14]:


np.eye(3)


# #### Use NumPy to generate a random number between 0 and 1

# In[16]:


np.random.rand(1)


# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

# In[17]:


np.random.randn(25)


# #### Create the following matrix:

# In[19]:


np.arange(0, 1.01, .01)


# #### Create an array of 20 linearly spaced points between 0 and 1:

# In[20]:


np.linspace(0, 1, 20)


# ## Numpy Indexing and Selection
# 
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

# In[21]:


mat = np.arange(1,26).reshape(5,5)
mat


# In[38]:


arr = np.array(([[12, 13, 14, 15], [17, 18, 19, 20], [22, 23, 24, 25]]))


# In[40]:





# In[42]:


arr[1, 3]


# In[41]:





# In[43]:


np.array(([[2],[7],[12]]))


# In[42]:





# In[44]:


np.arange(21, 26)


# In[46]:





# In[50]:


np.arange(16, 26).reshape(2,5)


# In[49]:





# ### Now do the following

# #### Get the sum of all the values in mat

# In[51]:


np.sum(mat)


# #### Get the standard deviation of the values in mat

# In[52]:


np.std(mat)


# #### Get the sum of all the columns in mat

# In[53]:


np.sum(mat, axis=0)


# # Great Job!
