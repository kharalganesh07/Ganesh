#!/usr/bin/env python
# coding: utf-8

# # Time Series Analysis

# In[2]:


#data cannot be independent
#ordering of data matters
#missing data not allowed


# In[3]:


import numpy as np 
import pandas as pd
from matplotlib import pyplot as plt

from statsmodels.tsa.seasonal import seasonal_decompose


# In[5]:


#read the data

df1= pd.read_csv('airpassenger.csv')


# In[6]:


df1.head()


# In[7]:


df1.tail()


# In[9]:


df1.shape


# In[12]:


df1.dtypes


# In[14]:


# we are trying to tell that we are trying to work with time series 

df1= pd.read_csv('airpassenger.csv',parse_dates=['Month'])


# In[15]:


df1.dtypes


# In[16]:


df1.head()


# In[17]:


df1.columns=['Month','Passengers']


# In[18]:


df1


# In[21]:


# it is recommended that we make our time series reference as the index

df1= pd.read_csv('airpassenger.csv',parse_dates=['Month'],index_col=['Month'])


# In[22]:


df1.head()


# In[23]:


# we can conviently do slicing i.e obtain data for a specific time period.

df1['1951-04-01':'1952-03-01']


# In[24]:


# we can check the values corresponding to a specific time plot

df1.loc['1951-12-01']


# In[27]:


# plot the time series

df1.plot()
plt.show()


# In[29]:


# increase the figure size

from pylab import rcParams
rcParams['figure.figsize']=15,8

df1.plot()
plt.show()


# In[31]:


# decompose the time series multiplicatively

df1_mul_decompose= seasonal_decompose(df1,model='multiplicative')
df1_mul_decompose.plot()
plt.show()


# In[34]:


df1.copy()


# In[35]:


# let's try to do log transformation
df1_log = df1.copy()


# In[36]:


df1_log['Passengers']= np.log(df1)


# In[39]:


df1_log.Passengers


# In[40]:


# visualize the log transformed series


# In[43]:


df1_log.plot()
plt.show()


# In[51]:


#compare the log transformed series

plt.subplot(2,1,1)
plt.title('Original Time series')
plt.plot(df1)

plt.subplot(2,1,2)
plt.title('Log time series')
df1_log.plot()
plt.tight_layout()
plt.show()


# In[ ]:




