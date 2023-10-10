#!/usr/bin/env python
# coding: utf-8

# # All imp Information 

# In[ ]:


#first perform the importing of all the library then perform 

data.head()


# In[ ]:


#import the data file in csv 

data= pd.read_csv('file_name.csv')


# # Data Pre-Processing

# In[ ]:


#after that perform

data.shape()
data.info()
data.describe()
data.


# In[ ]:


#perform the hist plot or any other plot to watch the data pattern

data['column_name'].hist(bins=20)
data.boxplot(column='column_name')


# In[ ]:


#if you see many outliers in any data through the boxplot and hist plot then normalize it using log function:
    
data['Log_column_name']=np.log(data['column_name'])


# # ====================================

# # Null value
To check the null value and replace it
# In[ ]:


#check weather the columns have the null data or not

data.isnull().sum()


# In[ ]:


#To fill up the catagorical null value put the condition like

data['column_name'].fillna(data['column_name'].mode()[0], inplace=True)


# In[ ]:


#for the numerical column

data.column_name= data.column_name.fillna(data.column_name.mean())

data['log_TotalIncome'].hist(bins=20)
# ====================================================

# In[1]:


#we also can handle the null value by using SimpleImputer

from sklearn.impute import SimpleImputer


# In[ ]:


imputer= SimpleImputer( missing_values=np.nan,
    strategy='mean')


# In[ ]:


#here it replace the missing values with the mean value for that row of the column
# here x is a independent variable where we stored the multiple column from index 0 to 2


imputer.fit(x[:,1:3])


# In[ ]:


x[:,1:3]= imputer.transform(x[:,1:3])


# In[ ]:





# In[ ]:





# In[ ]:


#Now assigning the dependent and independent variables

x= data.iloc[:,i,np.r_[0:5,9:11,13:15]] 

                 OR  (X = data.iloc[:, list(range(1, 6)) + list(range(9, 14))+ list(range(13,16))])

y= data.iloc[:,12]


# # ============================================================

# In[ ]:


#importing the library for the train test split

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2)


# # Categorical into numerical

# In[ ]:


# applying for loop for each of the index to be changed from catagorical to numeric
    #This is applicable when ther are more indices or column to be changed
    
    from sklearn.preprocessing import LabelEncoder
    
    for i in range(0,5):
    x_train[:,i]= labelencoder_x.fit_transform(x_train[:,i])
    
    x_train[:,7]= labelencoder_x.fit_transform(:,7)
    

    


# In[ ]:


#for the column to change into numerical from the catagorical we do as

labelencoder_y = LabelEncoder()

y_train = LabelEncoder_y.fit_transform(y_train)


# In[ ]:


# do same for the test variables too

for i in range(0,5):
    x_test[:,i]= labelencoder_x.fit_transform(x_test[:,i])
    
    x_test[:,7]= labelencoder_x.fit_transform(x_test[:,7])
    
    
    y_test= labelencoder_y.fit_transform(y_test)
    


# # Also in another way

# In[ ]:


# This creates the dummy numerical value for the every row in the column

from sklearn.preprocessing import OneHotEncoder

onehotencoder= OneHotEncoder
onehotencoder.fit_transform(dataset.col_name.values.reshape(-1,1)).toarray()


# This is done when there are more than two values in the column 

#otherwise the labelencoder works with the column with two different values like yes or no


# # Also Replacing Method

# In[ ]:


# Replacing the value in catagory form into numerical value directly

train['Loan_Status'].replace('N',0,inplace= True)
train['Loan_Status'].replace('Y',1,inplace= True)


# # standard scalar

# In[ ]:


# scale the dataset
#we have different data of different range 
#once we scaled data our analysis and prediction becomes much more better


# In[ ]:


from sklearn.preprocessing import StandardScaler
ss= StandardScaler()
x_train= ss.fit_transform(x_train)
x_test= ss. fit_transform(x_test)


# # Linear Regression
# 
# https://www.youtube.com/watch?v=x08AN87G0mg

# In[ ]:


# For importing the linear regression
 x= data['col']
 y= data['col']

 from sklearn.model_selection import train_test_split
 x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)

 from sklearn.linear_model import LinearRegression
 lr=LinearRegression()

 lr.fit(x_train,y_train) or 
lr.fit(np.array(x_train).reshape(-1,1),np.array(y_train).reshape(-1,1))

 y_predict=lr.pred(x_test)
    
 from sklearn.metrics import mean_squared_error
 mean_squared_error(y_test,y_pred)


# # Decision Tree Classifier

# In[ ]:


# import the library for decision tree


# In[ ]:


from sklearn.preprocessing import StandardScaler
ss= StandardScaler()
x_train= ss.fit_transform(x_train)
x_test= ss. fit_transform(x_test)


# In[ ]:


from sklearn.tree import DecisionTreeClassifier
DTClassifier = DecisionTreeClassifier(criterion = 'entropy', random_state=0)

DTClassifier.fit(x_train,y_train)


# In[ ]:


y_pred = DTClassifier.predict(x_test)
y_pred


# In[ ]:


# to find how well the prediction is 
#we can find the accuracy by 


from sklearn import metrics
print('the accuracy of decision tree =:',metrics.accuracy_score(y_pred,y_test)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




