#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns


# In[2]:


from matplotlib import pyplot as plt


# In[3]:


fmri=sns.load_dataset('fmri')


# In[12]:


fmri.head()


# In[13]:


fmri.shape


# In[14]:


sns.lineplot(x='timepoint',y='signal',data=fmri)
plt.show()


# In[19]:


sns.lineplot(x='timepoint',y='signal',data=fmri,hue='event')
plt.show()


# In[ ]:


sns.lineplot(x=)


# In[ ]:


#seaborn line plot


# In[20]:


sns.lineplot(x='timepoint',y='signal',data=fmri,hue='event',style='event',markers=True)
plt.show()


# In[9]:


sns.lineplot(x='timepoint',y='signal',data=fmri,hue='event',markers=True,style='event')
plt.show()


# In[10]:


#seaborn barplot


# In[11]:


import pandas as pd
sns.set(style='whitegrid')


# In[13]:


pk= pd.read_csv('pokemon.csv')


# In[15]:


pk.head()


# In[16]:


pk.tail()


# In[19]:


sns.barplot(x='is_legendary',y='speed',data=pk)
plt.show()


# In[20]:


sns.barplot(x='is_legendary',y='weight_kg', data = pk)
plt.show()


# In[21]:


sns.barplot(x='is_legendary',y='speed',hue='generation',data = pk)
plt.show()


# In[22]:


#pallates


# In[24]:


sns.barplot(x='is_legendary',y='speed',hue='generation',palette='Blues_d',data = pk)
plt.show()


# In[26]:


sns.barplot(x='is_legendary',y='weight_kg',palette='rocket', data = pk)
plt.show()


# In[27]:


sns.barplot(x='is_legendary',y='speed',hue='generation',palette='rocket',data = pk)
plt.show()


# In[28]:


sns.barplot(x='is_legendary',y='speed',hue='generation',palette='vlag',data = pk)
plt.show()


# In[30]:


sns.barplot(x='is_legendary',y='speed',hue='generation',color='green',data = pk)
plt.show()


# In[36]:


sns.barplot(x='is_legendary',y='weight_kg',color='green', data = pk)
plt.show()


# In[47]:


sns.barplot(x='is_legendary',y='weight_kg',color='blue', data = pk)
plt.show()


# In[48]:


#SEABORN SCATTERPLOT


# In[53]:


iris=pd.read_csv('iris.csv')


# In[54]:


iris.head()


# In[57]:





# In[58]:


sns.scatterplot(x='sepal_length',y='petal_length',data = iris)
plt.show()


# In[59]:


sns.scatterplot(x='sepal_length',y='petal_length',hue='species',data = iris)
plt.show()


# In[61]:


sns.scatterplot(x='sepal_length',y='petal_length',hue='petal_length',data = iris)
plt.show()


# In[70]:


#histogram plot


# In[71]:


import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# In[72]:


diamond=pd.read_csv('diamonds.csv')


# In[73]:


diamond.head()


# In[77]:


sns.distplot(diamond['price'])
plt.show()


# In[83]:


sns.histplot(diamond['price'])
plt.show()


# In[80]:


sns.distplot(diamond['price'],hist=False)
plt.show()


# In[91]:


sns.distplot(diamond['price'],color='purple')
plt.show()


# In[89]:


sns.distplot(diamond['price'],color='purple',hist=True, kde=False,bins=5)
plt.show()


# In[102]:


sns.distplot(diamond['price'],color='red',vertical=True)
plt.show()


# In[100]:


sns.distplot(diamond['price'],color='red',bins=5,kde=False,vertical=True)
plt.show()


# In[103]:


#JOINTPLOT


# In[106]:


sns.jointplot(x='sepal_length',y='petal_length',data= iris)
plt.show()


# In[107]:


sns.jointplot(x='sepal_length',y='petal_length',color='green',data= iris)
plt.show()


# In[111]:


sns.jointplot(x='sepal_length',y='petal_length',color='green',data= iris,kind='reg')
plt.show()


# In[112]:


#boxplot


# In[113]:


churn=pd.read_csv('Telecommunication_churn.csv')


# In[114]:


churn.head()


# In[119]:


sns.boxplot(x='Churn',y='tenure',data= churn,palette='rocket')
plt.show()


# In[124]:


sns.boxplot(x='InternetService',y='MonthlyCharges',data= churn,palette='Set1')
plt.show()


# In[125]:


sns.boxplot(x='InternetService',y='tenure',data= churn,palette='Set1')
plt.show()


# In[129]:


sns.boxplot(x='Contract',y='tenure',data=churn,linewidth=4,palette='Set1')
plt.show()


# In[133]:


sns.boxplot(x='Contract',y='tenure',data=churn,linewidth=4,palette='Set1',order =['One year','Two year','Month-to-month'] )
plt.show()


# In[134]:


sns.boxplot(x='Contract',y='tenure',data=churn,linewidth=4,palette='Set1',hue='PaymentMethod')
plt.show()


# In[135]:


#SEABORN PAIR PLOT


# In[136]:


iris.head()


# In[137]:


sns.pairplot(iris,hue='species')
plt.show()


# In[ ]:




