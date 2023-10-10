#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add():
    print('this is to add')


# In[2]:


add()


# In[6]:


def add(a,b):
   return a+b
    #print('the sum is' y )


# In[7]:


add(3,4)


# In[9]:


def oddoreven(x):
    if x%2==0:
        print(x, 'is even')
    else:
        print(x,'is odd')
        


# In[10]:


oddoreven(55)


# In[11]:


oddoreven(56)


# In[12]:


g = lambda x: x+ x*3


# In[13]:


g(7)


# In[15]:


g=(lambda x: (x%2!=0))


# In[17]:


g(4)


# In[18]:


l1=[12,3,67,43,5,8,4]
list1=list(filter(lambda x: (x%2!=0),l1))


# In[19]:


list1


# In[21]:


l1=[12,3,67,43,5,8,4]
list1=list(filter(lambda x: (x%2==0),l1))


# In[22]:


list1


# In[23]:


l1


# In[24]:


#lambda with map


# In[32]:


l2=[1,2,3,4,5,6,7]


# In[33]:


g2=list(map(lambda x: x+10,l2))


# In[35]:


g2


# In[41]:


from functools import reduce


# In[48]:


g3= reduce(lambda x,y: x+y*3-x*y,l1)


# In[49]:


g3


# In[1]:


## PRACTICE


# In[7]:


#def prime_num(x):
 #   i=o,count=0
 #   while(i!=x):
  #      if(x%i==0):
   #         count=count+1
    #i=i+1
    
  #  if count==2:
  #      print('Prime no')
   #
    #else :
     #   print('print not prime')


# In[22]:


def is_prime(num):
       for i in range(2,num):
           if (num%i)==0:
               return True
           
           return False


# In[23]:


is_prime(25)


# In[41]:


def isitprime(num):
    count=0
    for i in range(1,num+1):
        if (num%i)==0:
            count=count+1
            
        else:
            count=count
            
    if count>2:
        print('not prime')
            
    else:
        print(' prime')


# In[43]:


isitprime(12)


# In[ ]:




