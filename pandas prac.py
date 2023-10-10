#!/usr/bin/env python
# coding: utf-8

# In[73]:


#pandas 


# In[74]:


#pandas series object


# In[75]:


import pandas as pd


# In[76]:


s1=pd.array([1,2,3,4,5])


# In[77]:


s1


# In[78]:


s1=pd.Series([1,2,3,4,5])


# In[79]:


s1


# In[80]:


type(s1)


# In[81]:


s2=pd.Series(s1,index=['a','b','c','d','e'])


# In[82]:


s2


# In[83]:


s2=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])


# In[84]:


s2


# In[85]:


#series object with dictionary


# In[86]:


d1=pd.Series({'a':20,'b':30,'c':40})


# In[87]:


d1


# In[88]:


d1=pd.Series({'a':20,'b':30,'c':40}, index=('b','c','d','a'))


# In[89]:


d1


# In[90]:


d1[2]


# In[91]:


d1[1]


# In[92]:


l1=[1,2,3,4,5,6,7,8,9]


# In[93]:


s1=pd.Series(l1)


# In[94]:


s1


# In[95]:


s1[2]


# In[96]:


s1[:3]


# In[97]:


s1[-3:]


# In[98]:


s1 -100


# In[99]:


s1*5


# In[100]:


#pandas dataframe


# In[132]:


d1=pd.DataFrame=({'Name':['gk','mk','rk'],'marks':[20,30,40]})


# In[133]:


d1


# In[134]:


d1


# In[135]:


d1


# In[104]:


#dataframe builtin function


# In[137]:


iris=pd.read_csv('titanic.csv')


# In[138]:


iris.head()


# In[139]:


iris.tail()


# In[140]:


iris.shape


# In[143]:


iris.describe()


# In[144]:


iris.head()


# In[145]:


iris.iloc[0:5,0:3]


# In[146]:


iris.iloc[10:50,2:5]


# In[147]:


iris.loc[10:20,('Sex','Age')]


# In[148]:


iris.head()


# In[151]:


iris.drop('Ticket',axis=1)


# In[111]:


iris.drop([2,3,4],axis=0)


# In[154]:


iris.drop(2,axis=0 )


# In[155]:


iris.mean()


# In[113]:


iris.drop(['Name','Sex','Ticket'],axis=1)


# In[114]:


iris.drop(['Cabin','Embarked'],axis=1)


# In[115]:


iris.median()


# In[116]:


iris.min()


# In[117]:


iris.max()


# In[118]:


iris.mean()


# In[119]:


#more pandas function iloc


# In[120]:


iris.head()


# In[121]:


iris.iloc[5:11,:2]


# In[122]:


#iris.loc instead of column no and row no we should mention the row name and columnn name


# In[123]:


iris.loc[1:10,('Name','Parch','Ticket')]


# In[124]:


iris.head()


# In[125]:


def double_make(s):
    return s*2


# In[158]:


#iris.drop(2,axis=0)
iris[['Pclass','Ticket']].apply(double_make)


# In[157]:


#vlaue count value sort


# In[128]:


iris['Sex'].value_counts()


# In[129]:


iris.sort_values(by='Name')


# In[168]:


iris.sort_values(by='Sex')['Sex'].value_counts()


# In[ ]:





# In[ ]:




