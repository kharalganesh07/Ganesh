#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# In[2]:


ipl=pd.read_csv('matches.csv')


# In[3]:


ipl.head()


# In[4]:


ipl.tail()


# In[5]:


ipl.shape


# In[6]:


#getting the most freq of player of match
ipl['player_of_match'].value_counts()


# In[7]:


#getting the top 10 man of the matches
ipl['player_of_match'].value_counts()[0:10]


# In[8]:


#making the bar plot of top 5 man of the matches award


# In[9]:


key=list(ipl['player_of_match'].value_counts()[0:5].keys())
key


# In[ ]:





# In[10]:


#value=list(ipl['player_of_match'].value_counts()[0:5].values())


# In[11]:


plt.bar(key,list(ipl['player_of_match'].value_counts()[0:5]),color=['red','lime','blue','yellow','orange'])
plt.show()


# In[12]:


ipl['result'].value_counts()


# In[13]:


ipl['toss_winner'].value_counts()


# In[14]:


#finding the records where teams wins by runs that is it wins by batting first


# In[15]:


batfirst=ipl[ipl['win_by_runs']!=0]


# In[16]:


batfirst.head()


# In[17]:


#making a histogram
plt.figure(figsize=(8,5))
plt.hist(batfirst['win_by_runs'])
plt.title('distribution of runs')
plt.xlabel('runs margin')
plt.show()


# In[18]:


winnerbat=batfirst['winner'].value_counts()
winnerbat


# In[19]:


#finding out the most time winner with batting first


plt.figure(figsize=(5,5))
plt.bar(list(batfirst['winner'].value_counts()[0:3].keys()),list(batfirst['winner'].value_counts()[0:3]),color=['blue','yellow','red'])
plt.show()


#plt.bar(list(winnerbat.keys()[0:5]),list(winnerbat))
#plt.show()


# In[20]:


#win percentage by batting first


# In[21]:


plt.figure(figsize=(10,10))
plt.pie(list(batfirst['winner'].value_counts()),labels=list(batfirst['winner'].value_counts().keys()),autopct='%0.0f%%')
plt.show()


# In[22]:


#finding out the records where a team win by batting second or win by wickets


# In[23]:


batsecond=ipl[ipl['win_by_wickets']!=0]
batsecond.head()


# In[24]:


batsecond['winner'].value_counts()


# In[25]:


#finding out the top 4winner batting second

b2=batsecond['winner'].value_counts()[0:4]
b2


# In[26]:


#plotting top 5 in the barplot
plt.figure(figsize=(10,7))
plt.bar(b2.keys(),b2,color=['purple','blue','red','yellow'])
plt.title('No. of wins batting second',color='green')
plt.xlabel('Teams',color='green')
plt.ylabel('No of wins',color='green')
plt.show()


# In[27]:


#plotting in piechart


# In[28]:


plt.pie(b2,labels=b2[0:4].keys(),autopct='%0.0f%%',colors=['purple','blue','red','yellow'])
plt.show()


# In[29]:


#finding out the histogram to show relation between the no of wins wrt no of wickets
#histogram is usually made for the column having numerical value


# In[30]:


batsecond.head()


# In[31]:


plt.hist(batsecond['win_by_wickets'],bins=20)
plt.show()


# In[32]:


#looking at the most no of matches per season


# In[33]:


most=ipl['season'].value_counts()
most


# In[34]:


plt.bar(most.keys(),most)


# In[73]:


ipl.head()


# In[77]:


toss_winner = ipl['toss_winner'].value_counts()
toss_winner


# In[88]:


toss_winner1= ipl[ipl['winner']==ipl['toss_winner']]
toss_winner1.head()
#toss_winner1.shape


# In[86]:


toss_winner2= (ipl['toss_winner']==ipl['winner']).value_counts()
toss_winner2


# In[91]:


toss_winner3=toss_winner1['winner'].value_counts()
toss_winner3


# In[97]:


plt.figure(figsize=(15,8))
plt.bar(toss_winner3.keys()[0:5],toss_winner3[0:5])


# In[ ]:





# In[35]:


#looking at the number of matches per city


# In[36]:


mostcity=ipl['city'].value_counts()
mostcity


# In[37]:


#loading out how many times a team wins the match after winning the toss


# In[38]:


tosswinner=np.sum(ipl['winner']==ipl['toss_winner'])
tosswinner


# In[39]:


tosswinner/sum(ipl['id'].value_counts())


# # Another csv file[Deliveries]

# In[40]:


delivery=pd.read_csv('deliveries.csv')


# In[41]:


delivery.head()


# In[42]:


delivery.shape


# In[43]:


delivery['match_id'].unique()


# In[44]:


delivery.head()


# In[45]:


match1=delivery[delivery['match_id']==1]


# In[46]:


match1.head()


# In[47]:


match1.shape


# In[48]:


kkr=match1[match1['inning']==1]


# In[49]:


kkr.head()


# In[50]:


kkr['batsman_runs'].value_counts()


# In[51]:


rcb=match1[match1['inning']==2]
rcb.head()


# In[52]:


rcb['batsman_runs'].value_counts()


# In[53]:



sum(kkr['batsman_runs'].value_counts())


# In[54]:


sum(rcb['batsman_runs'].value_counts())


# In[55]:


kkr['player_dismissed'].value_counts()


# In[56]:


sum(kkr['player_dismissed'].value_counts())


# In[57]:


rcb['player_dismissed'].value_counts()


# In[58]:


sum(rcb['player_dismissed'].value_counts())


# In[59]:


rcb['dismissal_kind'].value_counts()


# In[60]:


ipl.head()


# In[61]:


iplsort=ipl[['id','team1','team2','winner','player_of_match']]


# In[62]:


iplsort.head()


# In[63]:


delivery


# In[100]:


batsmanruns=delivery[['match_id','batsman','batsman_runs']]
batsmanruns.head(20)


# In[65]:


batsmanruns.sort_values(by=['batsman_runs'],ascending=False)[0:20]


# In[66]:


batsmanruns1=batsmanruns[batsmanruns['match_id']==1]


# In[67]:


batsmanruns1.head()


# In[68]:


batsmanruns1.groupby(['batsman'],as_index =False)['batsman_runs'].sum().sort_values(by='batsman_runs',ascending =False)


# In[69]:


ipl.head()


# In[70]:


delivery.groupby(['batsman'],as_index =False)['batsman_runs'].sum().sort_values(by='batsman_runs',ascending =False)[0:10],


# In[ ]:





# In[71]:


#batsmanruns1['batsman',['batsman_runs'].value_counts()]


# In[72]:


batsmanruns1['batsman_runs'].value_counts(),groupby('')


# In[ ]:


b1=batsmanruns1.groupby('batsman_runs')


# In[ ]:


b1


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




