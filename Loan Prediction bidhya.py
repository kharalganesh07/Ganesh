#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot  as plt
import warnings
warnings.filterwarnings('ignore')


# In[49]:


train= pd.read_csv('train_loan.csv')
test = pd.read_csv('test_loan.csv')


# In[157]:


train.head(20)


# In[51]:


test.head()


# In[52]:


train.info()


# In[53]:


train.describe()


# In[54]:


train.isnull().sum()


# In[55]:


train.columns


# In[56]:


train.dtypes


# In[57]:


train.shape


# In[58]:


test.shape


# In[59]:


# Lets look the frequency table, percentage distribution and bar plot of
# the target variable ie. Loan_status

train['Loan_Status'].value_counts()


# In[60]:


train['Loan_Status'].value_counts(normalize= True)


# In[61]:


train['Loan_Status'].value_counts().plot.bar()


# In[62]:


plt.figure(figsize=(4,5))
plt.bar(train['Loan_Status'].value_counts().keys(),train['Loan_Status'].value_counts())
plt.show()


# In[63]:


# Let's visualize the catagorical and the ordinal columns


# In[64]:


plt.figure(1)
plt.subplot(2,2,1)
train['Gender'].value_counts(normalize=True).plot.bar(figsize=(20,20),title='Gender')


plt.subplot(2,2,2)
train['Married'].value_counts(normalize=True).plot.bar(figsize=(5,5),title='Married')

plt.subplot(2,2,3)
train['Self_Employed'].value_counts(normalize=True).plot.bar(title= 'Self_Employed')

plt.subplot(2,2,4)
train['Credit_History'].value_counts(normalize = True).plot.bar(title='Credit History')


# In[65]:


# 80% of the applicants are male
# Around 65% of the applicants are married
# 


# In[66]:


# independent variable (Ordinal)


# In[67]:


train.head()


# In[68]:


plt.figure(1)
plt.subplot(1,3,1)
train['Dependents'].value_counts(normalize = True).plot.bar(figsize= (24,6),title= "Dependents")


plt.subplot(1,3,2)
plt.bar(train['Education'].value_counts(normalize= True).keys(),train['Education'].value_counts(normalize= True))
plt.title(' Education')

plt.subplot(1,3,3)
train['Property_Area'].value_counts(normalize = True).plot.bar(title='Property Area')


# In[69]:


# independent variable (Numerical value)


#lets analyze and visualize it using the histplot or distplot and boxplot


# In[72]:


plt.figure(1)
plt.subplot(1,2,1)
train['ApplicantIncome'].plot.box(figsize=(16,5))

plt.subplot(1,2,2)
sns.distplot(train['ApplicantIncome'])


# In[79]:


plt.figure(figsize=(20,5))
plt.subplot(1,2,2)
sns.histplot(train['ApplicantIncome'])


# In[80]:


# since most of the data  is in the left side so it is not normally distributed
# we will try to make it normal later 

# from the boxplot also we can see that there are a lot of outliers 


# In[82]:


# lets segregrate them by educatin using boxplot


# In[85]:


train.boxplot(column='ApplicantIncome', by ="Education")


# In[86]:


# those who are graduated have more than that of non-graduate


# In[90]:


plt.figure(1)
plt.subplot(1,2,1)
sns.distplot(train['CoapplicantIncome'])
plt.title("distplot of Coapplicant INcome")

plt.subplot(1,2,2)
train['CoapplicantIncome'].plot.box(figsize=(16,5), title='Coapplicantincome')


# In[91]:


# The data is seeing to be left in the distplot so it is not normally distributed
# There are many outliers in the boxplot so the data should be managed 


# In[92]:


# lets on LoanAmount 


# In[93]:


plt.figure(1)
plt.subplot(1,2,1)
sns.distplot(train['LoanAmount'])
plt.title("distplot of LoanAmount")

plt.subplot(1,2,2)
train['LoanAmount'].plot.box(figsize=(16,5), title='LoanAmount')


# In[94]:


# Here the data seems to be  fairly normally distributed in the dist diagram
# But there are some outliers in the boxplot


# # Bivariate Analysis

# In[95]:


# some of the hypothesis are made 
# 1.Applicants with high income should have more chances of loan approval
#2. Applicants who have repaid their previous dbts should have higher chances of loan approval
#3. loan approval should also depend upon the loan amount. Higher the amount lower the chance of loan approval and vice versa
#4. Lesser the amount to be paid monthly to repay the loan, higher the chances of loan approval


# In[97]:


#Catagorical Independent variable vs Target Variable

# finding the relation between the target and the categorical independent variable


# In[108]:


Gender1 = pd.crosstab(train['Gender'], train['Loan_Status'])

Gender1.div(Gender1.sum(1).astype(float),axis=0).plot.bar(stacked=True , figsize=(4,4))



# In[110]:


Gender1.div(Gender1.sum(1).astype(float),axis=0).plot.bar(stacked=False , figsize=(4,4))


# In[119]:


married= pd.crosstab(train['Married'],train['Loan_Status'])
married.div(married.sum(1).astype(float),axis=0).plot.bar(stacked=True, figsize=(4,4))


# In[120]:


#education dependents, self_employed
education= pd.crosstab(train['Education'],train['Loan_Status'])
education.div(education.sum(1).astype(float),axis=0).plot.bar(stacked=True, fig=(4,4))


# In[122]:


dependents=pd.crosstab(train['Dependents'],train['Loan_Status'])
dependents.div(dependents.sum(1).astype(float),axis=0).plot.bar(stacked=True, figsize=(4,4))


# In[123]:


selfemployed=pd.crosstab(train['Self_Employed'],train['Loan_Status'])
selfemployed.div(selfemployed.sum(1).astype(float),axis=0).plot.bar(stacked=True, figsize=(4,4))


# In[124]:


#proportion of married applicants is higher for the approved loan
#distribution of applicants with1 or 3 dependents is simillar across both the
#.....................


# In[125]:


Credit_History=pd.crosstab(train['Credit_History'],train['Loan_Status'])
Credit_History.div(Credit_History.sum(1).astype(float),axis=0).plot.bar(stacked=True, figsize=(4,4))


Property_Area=pd.crosstab(train['Property_Area'],train['Loan_Status'])
Property_Area.div(Property_Area.sum(1).astype(float),axis=0).plot.bar(stacked=True, figsize=(4,4))


# In[126]:


# Numerical independent variable vs target variable


# In[128]:


train.groupby('Loan_Status')['ApplicantIncome'].mean().plot.bar()

# Here the y-axis represent the mean applicant income. we don't see any changes in the mean income
# so let's make bins for the applicant income variable based on the values in it and analyze the corrosponding loan status for each bean

# In[140]:


#to view the data ranges 
train['ApplicantIncome'].plot.box()


# In[138]:


bins = [0,2500,4000,6000,81000]
group =['low','average','high','very_high']
train['Income_bin']=pd.cut(train['ApplicantIncome'],bins,labels=group)


# In[139]:


Income_bin = pd.crosstab(train['Income_bin'], train['Loan_Status'])
Income_bin.div(Income_bin.sum(1).astype(float),axis=0).plot.bar(stacked=True,figsize =(4,4))


# In[142]:


train['LoanAmount'].plot.box()


# In[149]:


bins=[0,100,200,700] 
group=['low','average','high']
train['loanamount_bin']= pd.cut(train['LoanAmount'],bins,labels=group)


# In[150]:


loanamount_bin= pd.crosstab(train['loanamount_bin'],train['Loan_Status'])
loanamount_bin.div(loanamount_bin.sum(1).astype(float),axis=0).plot.bar(stacked= True, figsize= (4,4))


# In[152]:


# here the applicants with higher loanamount has the less chances of loan approval


# In[ ]:


train= train.drop(['Income_bin','loanamount_bin'],axis=1)


# # Missing value and Outlier Treatment

# In[8]:


train1= pd.read_csv('train_loan.csv')
test1 = pd.read_csv('test_loan.csv')
original_train1 = train1.copy()


# In[9]:


train1.head()


# In[11]:


train1.shape


# In[12]:


# Changing the categorical value of loan status from y/n to 1/0 by replacing it directly
# changing the value 3+ value into 3 


# In[6]:


train1['Loan_Status'].replace('N',0,inplace= True)
train1['Loan_Status'].replace('Y',1,inplace= True)


# In[13]:


train1['Dependents'].replace('3+', 3, inplace = True)
test1['Dependents'].replace('3+', 3, inplace = True)


# In[14]:


train1.head()

Missing Value Imputation

# In[15]:


train1.isnull().sum()


# In[16]:


# For numerical values --> imputation using mean or median
# for categorical values --> imputation using mode


# In[18]:


train1['Gender'].fillna(train1['Gender'].mode()[0],inplace= True)
train1['Married'].fillna(train1['Married'].mode()[0],inplace = True)
train1['Self_Employed'].fillna(train1['Self_Employed'].mode()[0],inplace = True)

train1['Dependents'].fillna(train1['Dependents'].mode()[0],inplace = True)


# In[19]:


# since Loan amount term is the numerical colunmn but the value 360 is repeatedd mostly
# so we perform the mode in it


# In[20]:


train1['Loan_Amount_Term'].fillna(train1['Loan_Amount_Term'].mode()[0],inplace = True)


# In[21]:


train1.isnull().sum()


# In[227]:


# for the catagorical value


# In[22]:


train1['LoanAmount'].fillna(train1['LoanAmount'].median(),inplace= True)
   


# In[23]:


train1['Credit_History'].fillna(train1['Credit_History'].median(),inplace= True)


# In[25]:


train1.isnull().sum()


# In[26]:


# to count the NaN value in the loanamount
nan_count = train1['LoanAmount'].isna().sum()
nan_count


# In[233]:





# In[27]:


train1.shape


# In[28]:


train1.head()


# In[30]:


# Lets do it for the test data set too

test1['Gender'].fillna(test1['Gender'].mode()[0],inplace= True)
test1['Married'].fillna(test1['Married'].mode()[0],inplace = True)
test1['Self_Employed'].fillna(test1['Self_Employed'].mode()[0],inplace = True)

test1['Dependents'].fillna(test1['Dependents'].mode()[0],inplace = True)


test1['Loan_Amount_Term'].fillna(test1['Loan_Amount_Term'].mode()[0],inplace = True)


# In[35]:


test1.isnull().sum()


# In[34]:


# Now for the categorical value of the test data set
 test1['LoanAmount'].fillna(train1['LoanAmount'].median(),inplace = True)


# In[ ]:




