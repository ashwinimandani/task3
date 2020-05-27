#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


admissions=pd.read_csv("Admission_Predict.csv")
admissions.head()


# In[3]:


admissions.corr()
admissions.columns
X=admissions[['GRE Score', 'TOEFL Score', 'University Rating', 'SOP',
       'LOR ', 'CGPA', 'Research']]
y=admissions['Chance of Admit ']
admissions.corr()


# In[4]:


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# In[5]:


model=LinearRegression()
x_train,x_test,y_train,y_test=train_test_split(X,y,random_state=42)


# In[6]:


model.fit(x_train,y_train)


# In[7]:


model.predict(x_test)
((0.68-0.64916133)/0.68)*100


# In[8]:


from sklearn.linear_model import Lasso
from sklearn.feature_selection import SelectFromModel


# In[9]:


model_selection=SelectFromModel(Lasso())


# In[10]:


model_selection.fit(X,y)
model_selection.get_support()


# In[11]:


X=X['GRE Score']


# In[17]:


x_train,x_test,y_train,y_test=train_test_split(X,y,random_state=42)
x_train=x_train.values.reshape(-1,1)


# In[18]:


model.fit(x_train,y_train)


# In[21]:


model.predict(x_test.values.reshape(-1,1))


# In[ ]:


(0.68-0.65362181)/0.68


# ## Wrapper 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




