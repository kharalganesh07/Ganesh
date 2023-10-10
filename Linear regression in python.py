#!/usr/bin/env python
# coding: utf-8

# In[2]:



import pandas as pd


# In[3]:


iris=pd.read_csv('iris.csv')


# In[4]:


iris.head(10)


# In[5]:


iris['sepal_width']>4


# In[6]:


iris[iris['sepal_width']>4]


# In[7]:


iris[iris['petal_width']>1]


# In[8]:


iris[iris['petal_width']>2]


# In[9]:


from matplotlib import pyplot as plt 


# In[10]:


import seaborn as sns


# In[11]:


sns.scatterplot(x='sepal_length',y='petal_length',data =iris)
plt.show()


# In[12]:


sns.scatterplot(x='sepal_length',y='petal_length',data =iris,hue='species')
plt.show()


# In[13]:


sns.scatterplot(x='sepal_length',y='petal_length',data =iris,hue='petal_width')
plt.show()


# # linear regression 
Iris file csv
# In[14]:


iris.head()


# In[15]:


#want to know how the sepal length will change according to sepal width


# In[16]:


y=iris[['sepal_length']]
x=iris[['sepal_width']]


# In[17]:


#training and testing variable


# In[18]:


#   sklearn is used to implement the algorithm models


# In[19]:


from sklearn.model_selection import train_test_split


# In[20]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)


# In[21]:


x_train.head()


# In[22]:


x_test.head()


# In[23]:


y_train.head()


# In[24]:


y_test.head()


# In[25]:


from sklearn.linear_model import LinearRegression


# In[26]:


lr= LinearRegression()
lr


# In[27]:


lr.fit(x_train,y_train)


# In[28]:


y_pred=lr.predict(x_test)
y_pred


# In[29]:


y_test.head()


# In[30]:


y_pred[0:5]


# In[31]:


# from above here we can find the y_pred value for the y value


# In[32]:


# now finding the ERROR IN PREDICTION


# In[33]:


from sklearn.metrics import mean_squared_error


# In[34]:


mean_squared_error(y_test,y_pred)


# # model 2

# In[35]:


y=iris[['sepal_length']]


# In[36]:


x=iris[['sepal_width','petal_length','petal_width']]


# In[37]:


from sklearn.model_selection import train_test_split


# In[38]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)


# In[39]:


lr2=LinearRegression()


# In[40]:


lr2.fit(x_train,y_train)


# In[41]:


y_pred2=lr2.predict(x_test)


# In[42]:


mean_squared_error(y_test,y_pred2)


# # Linear Regression for covid 19 datasets
Visualization
# In[43]:


import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import datetime as dt


# In[44]:


#importing data sets of covid 19 india
df=pd.read_csv('covid_19_india.csv',parse_dates=['Date'],dayfirst=True)


# In[45]:


df.head()


# In[46]:


df.tail()


# In[47]:


df= df[['Date','State/UnionTerritory','Cured','Deaths','Confirmed']]


# In[48]:


df


# In[49]:


df.info()


# In[50]:


df.columns=['date','state','cured','deaths','confirmed']


# In[51]:


df.head()


# In[52]:


df.tail()

df
# In[53]:


(df['state']).value_counts()


# In[54]:


today=df[df['date']=='2020-06-22']
today


# In[55]:


today.head()


# In[56]:


#sorting data wrt number of confirmed cases
max_confirmed_cases= today.sort_values(by='confirmed',ascending=False)
max_confirmed_cases


# In[57]:


max_confirmed_cases.shape


# In[60]:


max_10_confirmed=today.sort_values(by='confirmed',ascending=False)[0:10]
max_10_confirmed


# In[71]:


plt.figure(figsize=(15,5))
sns.barplot(x='state',y='confirmed',data=max_10_confirmed)
plt.show()


# In[73]:


max_deaths=today.sort_values(by=['deaths'],ascending=False)
max_deaths


# In[74]:


max_10_deaths=max_deaths[0:10]
max_10_deaths


# In[77]:


plt.figure(figsize=(15,5))
sns.barplot(x='state',y='deaths',data=max_10_deaths,hue='state')


# In[78]:


max_cured=today.sort_values(by=['cured'],ascending=False)[0:8]
max_cured


# In[103]:


max_number2=today.groupby(['state'],as_index=False)['cured'].sum().sort_values(by=['state'],ascending=False)[0:8]
max_number2


# In[112]:


max_number3=today.groupby(['state'],as_index=False)['cured','deaths'].sum().sort_values(by=['state'],ascending=False)
max_number3


# In[113]:


df.head()


# In[123]:


delh=df[['state','cured']]
delh


# In[126]:


maha=df[df.state=='Maharashtra']


# In[127]:


maha


# In[134]:


#visualizing the confirmed cases in maharashtra
plt.figure(figsize=(15,5))
sns.lineplot(x='date',y='confirmed',data=df)
plt.show()


# In[133]:


plt.figure(figsize=(15,5))
sns.lineplot(x='date',y='confirmed',data=maha,color='green')
plt.show()


# In[135]:


plt.figure(figsize=(15,5))
sns.lineplot(x='date',y='deaths',data=maha,color='red')
plt.show()


# In[139]:


delhi=df[df.state=='Delhi']
delhi


# In[144]:


plt.figure(figsize=(10,5))
sns.lineplot(x='date',y='confirmed',data=delhi)
plt.show()


# In[145]:


haryana=df[df.state=='Haryana']
haryana


# In[150]:


plt.figure(figsize=(10,5))
sns.lineplot(x='date',y='confirmed',data=haryana)
plt.show()


# In[152]:


plt.figure(figsize=(20,5))
sns.barplot(x='date',y='confirmed',data=haryana)
plt.show()


# # Linear Regression

# In[154]:


from sklearn.model_selection import train_test_split


# In[155]:


maha


# In[203]:


#converting the date-time to ordinal
maha['date']=maha['date'].map(dt.datetime.toordinal)
maha.head()


# In[244]:


x= maha['date']
y= maha['confirmed']


# In[245]:


#training and testing check


# In[246]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)


# In[247]:


x_train.head()


# In[248]:


x_test.head()


# In[249]:


from sklearn.linear_model import LinearRegression


# In[250]:


lr1=LinearRegression


# In[251]:


#from sklearn.ensemble import RandomForestRegressor
#rfr=RandomForestRegressor()
#rfr.fit(np.array(x_train).reshape(-1,1),np.array(y_train).reshape(-1,1))


# In[252]:


#lr1.fit(np.array(x_train).reshape(-1,1),np.array(y_train).reshape(-1,1))


# In[253]:


#y_predict=y_pred(x_test)


# In[254]:


y_train


# In[256]:


maha.tail()


# In[257]:


#lr1.fit(y,y)


# In[ ]:





# In[ ]:





# In[ ]:




