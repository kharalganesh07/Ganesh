#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


data=pd.read_csv("Loan_Data.csv")


# In[3]:


data.head()


# In[4]:


data.shape


# In[5]:


data.info()


# In[6]:


data.describe()


# In[7]:


#Crosstab between loan status and credit history
pd.crosstab(data['Credit_History'], data['Loan_Status'],margins=True)


# In[8]:


#boxplot for Applicant Income variable
plt.boxplot(data['ApplicantIncome'])


# In[9]:


data.boxplot(column='ApplicantIncome')


# In[10]:


data['ApplicantIncome'].hist(bins=20)


# In[11]:


data['CoapplicantIncome'].hist(bins=20)


# In[12]:


data.head(
)


# In[13]:


data.boxplot(column='ApplicantIncome',by='Education')


# In[14]:


data.boxplot(column='LoanAmount')


# In[15]:


plt.boxplot(data['LoanAmount'])


# In[16]:


data['LoanAmount'].hist(bins=20)


# In[17]:


data['log_LoanAmount']=np.log(data['LoanAmount'])
data['log_LoanAmount'].hist(bins=20)


# In[18]:


data.isnull().sum()


# In[19]:


data['Gender'].fillna(data['Gender'].mode()[0],inplace=True)


# In[20]:


data['Dependents'].fillna(data['Dependents'].mode()[0],inplace=True)


# In[21]:


data['Married'].fillna(data['Married'].mode()[0],inplace=True)


# In[22]:


data['Self_Employed'].fillna(data['Self_Employed'].mode()[0],inplace=True)


# In[23]:


data.Loan_Amount_Term=data.Loan_Amount_Term.fillna(data.Loan_Amount_Term.mean())


# In[24]:


data.LoanAmount=data.LoanAmount.fillna(data.LoanAmount.mean())


# In[25]:


data.log_LoanAmount=data.log_LoanAmount.fillna(data.log_LoanAmount.mean())


# In[26]:


data['Credit_History'].fillna(data['Credit_History'].mode()[0],inplace=True)


# In[27]:


data.isnull().sum()


# In[28]:


# we now normalize the data of applicant income and coapplicant income
#instead of doing it separately we do it by adding

data['Total_Income']=data['ApplicantIncome']+ data['CoapplicantIncome']
data['log_TotalIncome']=np.log(data['Total_Income'])

data['log_TotalIncome']


# In[29]:


data['log_TotalIncome'].hist(bins=20)


# In[30]:


data.head(10)


# # Decision tree classifier

# In[56]:


x=data.iloc[:,np.r_[1:5,9:11,13:15]].values
y=data.iloc[:,12].values


#X = data.iloc[:, list(range(1, 6)) + list(range(9, 14))+ list(range(13,16))]
#y= data.iloc[:,12]


# In[59]:


x


# In[60]:


y


# In[64]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)


# In[65]:


print(x_train)


# In[66]:


#using labelencoder changing the categorical column into numerical values


# In[67]:


from sklearn.preprocessing import LabelEncoder

#creating instance for labelencoder
labelencoder_x= LabelEncoder()


# In[68]:


# applying for loop for each of the index to be changed from catagorical 
# to numeric


# In[69]:


for i in range(0,5):
    x_train[:,i]= labelencoder_x.fit_transform(x_train[:,i])


# In[71]:


x_train[:,7]= labelencoder_x.fit_transform(x_train[:,7])


# In[72]:


x_train


# In[75]:


labelencoder_y = LabelEncoder()

y_train= labelencoder_y.fit_transform(y_train)


# In[77]:


y_train


# In[78]:


for i in range(0,5):
    x_test[:,i]= labelencoder_x.fit_transform(x_test[:,i])
    
    x_test[:,7]= labelencoder_x.fit_transform(x_test[:,7])


# In[79]:


y_test= labelencoder_y.fit_transform(y_test)


# In[80]:


x_test


# In[81]:


y_test


# In[82]:


# scale the dataset
#we have different data of different range 
#once we scaled data our analysis and prediction becomes much more better


# In[139]:


from sklearn.preprocessing import StandardScaler
ss= StandardScaler()
x_train= ss.fit_transform(x_train)
x_test= ss. fit_transform(x_test)


# In[140]:


from sklearn.tree import DecisionTreeClassifier
DTClassifier = DecisionTreeClassifier(criterion = 'entropy', random_state=0)

DTClassifier.fit(x_train,y_train)


# In[141]:


y_pred = DTClassifier.predict(x_test)
y_pred


# In[142]:


from sklearn import metrics
print('the accuracy of decision tree is:',metrics.accuracy_score(y_pred,y_test))


# # Naive based Classifier

# In[143]:


from sklearn.naive_bayes import GaussianNB
NBClassifier = GaussianNB()
NBClassifier.fit(x_train,y_train)


# In[144]:


y_pred = NBClassifier.predict(x_test)


# In[145]:


y_pred


# In[146]:


print('the accuracy is :',metrics.accuracy_score(y_pred,y_test))


# In[147]:


#Import test datas sets


# In[148]:


data.head()


# In[149]:


testdata= pd.read_csv('loan-test.csv')


# In[150]:


testdata.head()


# In[151]:


testdata.info()


# In[152]:


testdata.isnull().sum()


# In[153]:


testdata['Gender'].fillna(testdata['Gender'].mode()[0],inplace=True)


# In[154]:


testdata['Dependents'].fillna(testdata['Dependents'].mode()[0],inplace=True)
testdata['Self_Employed'].fillna(testdata['Self_Employed'].mode()[0],inplace=True)
testdata['Loan_Amount_Term'].fillna(testdata['Loan_Amount_Term'].mode()[0],inplace = True)
testdata['Credit_History'].fillna(testdata['Credit_History'].mode()[0],inplace = True)


# In[155]:


testdata.LoanAmount= testdata.LoanAmount.fillna(testdata.LoanAmount.mean())


# In[156]:


testdata.isnull().sum()


# In[157]:


testdata.boxplot(column="LoanAmount")


# In[158]:


testdata['loanamount_log']= np.log(testdata['LoanAmount'])


# In[159]:


testdata['totalincome']= testdata['ApplicantIncome']+ testdata['CoapplicantIncome']


# In[160]:


testdata['totalincome_log']= np.log(testdata['totalincome'])


# In[161]:


testdata.head()


# In[162]:


test= testdata.iloc[:,np.r_[1:5,9:11,13:15]].values


# In[163]:


for i in range(0,5):
    test[:,i]=labelencoder_x.fit_transform(test[:,i])


# In[164]:


test[:,7]=labelencoder_x.fit_transform(test[:,7])


# In[165]:


test


# In[166]:


#scaling the data 
test= ss.fit_transform(test)


# In[167]:


pred= NBClassifier.predict(test)


# In[168]:


pred


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




