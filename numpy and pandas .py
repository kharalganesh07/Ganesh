#!/usr/bin/env python
# coding: utf-8

# In[1]:


#numpy


# In[2]:


import numpy as np


# In[3]:


n1=np.array([10,20,30,40])


# In[4]:


n1


# In[5]:


type(n1)


# In[6]:


n1=np.array([10,20,30,40])


# In[7]:


n2=np.array([[10,20,30],[50,60,70]])


# In[8]:


n2


# In[9]:


type(n2
    )


# In[10]:


#zeros array


# In[11]:


n3=np.zeros((1,2))


# In[12]:


n3


# In[13]:


n3=np.zeros((2,2))


# In[14]:


n3


# In[15]:


n3=np.zeros((10,10))
n3


# In[16]:


type(n3)


# In[17]:


#full array= initializing numpy with same number


# In[18]:


n1=np.full((2,3),5)
n1


# In[19]:


#arrange initializing numpy array within a range


# In[20]:


n1=np.arange(50,101)


# In[21]:


n1


# In[22]:


n2=np.arange(10,300,10)


# In[23]:


n2


# In[24]:


#randam number initialoization


# In[25]:


n3= np.random.randint(1,500,10)


# In[26]:


n3


# In[27]:


n3


# In[28]:


#numpy shape


# In[29]:


n1=np.array([[1,2,3,4],[5,6,7,8]])


# In[30]:


n1


# In[31]:


n1.shape


# In[32]:


n1.shape =(4,2)


# In[33]:


n1


# In[34]:


#joining numpy arrays


# In[35]:


n1=np.array([10,20,30])
n2=np.array([40,50,60])


# In[36]:


n3=np.vstack((n1,n2))


# In[37]:


n3


# In[38]:


n4=np.hstack((n1,n2))
n4


# In[39]:


n5=np.column_stack((n1,n2))


# In[40]:


n5


# In[41]:


#numpy intersection and difference


# In[42]:


n1=([10,20,30,40,50,60])
n2=([50,60,70,80,90,100])


# In[43]:


n3=np.intersect1d(n1,n2)


# In[44]:


n3


# In[45]:


n4= np.setdiff1d(n1,n2)
n4


# In[46]:


n5=np.setdiff1d(n2,n1)
n5


# In[47]:


#numpy array maths addition


# In[48]:


np.sum([n1,n2])


# In[49]:


np.sum([n1,n2],axis=0)


# In[50]:


#addition subtraction multiplication to each value


# In[51]:


n1=np.array([1,2,3])
n2=np.array([5,6,7])


# In[52]:


n1+5


# In[53]:


n1


# In[54]:


n1=n1+10


# In[55]:


n1


# In[56]:


med=np.median(n1)


# In[57]:


med


# In[58]:


avg=np.mean(n2)
avg


# In[59]:


np.std(n1)


# In[60]:


#save aand load the numpy


# In[61]:


np.save('mysave',n1)


# In[62]:


newn1=np.load('mysave.npy')


# In[63]:


newn1


# In[67]:


n1=np.array([2,5,7,3,5,8,16,4,52,5])


# In[68]:


n1


# In[83]:


n2=([2,3,4,5],[7,8,9,41])


# ## 

# In[84]:


np.vstack(n2)


# In[85]:


n2


# In[86]:


d2=np.zeros([2,2])
d2


# In[87]:


list=np.arange(1,200,10)
list


# In[88]:


l=np.random.randint(1,100,10)


# In[89]:


l


# In[ ]:




