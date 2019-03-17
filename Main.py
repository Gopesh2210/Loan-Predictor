#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import pickle


# In[2]:


df = pd.read_csv('credit_train_edited_version.csv')
df.info()


# In[3]:


df.head()


# In[4]:


df_b = df.drop(['Loan ID','Customer ID','Loan Status'],axis=1)


# In[5]:


df_b.head()


# In[6]:


df_b.info()


# In[ ]:





# In[7]:


tmp = df['Years in current job'].astype('str')


# In[27]:


for i in range(0,len(tmp)):
    x = tmp[i].split()
    if(x[0] == '<'):
        tmp[i] = x[1]
    else:
        tmp[i] = x[0]
    


# In[29]:


for i in range(0,len(tmp)):
    if(tmp[i].isdigit()):
        tmp[i] = int(tmp[i])
    else:
        tmp[i] = int(tmp[i][:2])


# In[60]:


df_b= df_b.drop(['Years in current job'],axis=1)


# In[61]:


df_b.head()


# In[62]:


df_b = pd.concat([df_b,tmp],axis=1)


# In[66]:


df_b.info()


# In[71]:


df_b['Years in current job']=pd.to_numeric(df_b['Years in current job'])


# In[72]:


df_b.info()


# In[73]:


df_b.to_csv(r'./data_set.csv',index=False)


# In[32]:


X = df_b.drop(['Fully Paid','Term','Purpose','Home Ownership'],axis=1)


# In[33]:


Y = df_b['Fully Paid']


# In[34]:


X_trn,X_tst,Y_trn,Y_tst = train_test_split(X,Y,test_size=0.05,random_state=42)


# In[84]:


rc = RandomForestClassifier(n_estimators=1000)


# In[85]:


rc.fit(X_trn,Y_trn)


# In[88]:


pc = rc.predict(X_tst)
print classification_report(Y_tst,pc)
print confusion_matrix(Y_tst,pc)


# In[2]:





# In[90]:


model = "trainedModel.sav"
pickle.dump(rc, open(model, 'wb'))


# In[98]:


plt.plot(y=rc.feature_importances_,x = X.columns)


# In[99]:


imp = rc.feature_importances_


# In[100]:


len(imp)


# In[101]:


len(X.columns)


# In[102]:


plt.barh(X.columns,imp)


# In[11]:


filename = "trainedModel.sav"
rc = pickle.load(open(filename,'rb'))


# In[12]:


df = pd.read_csv('data_set.csv')
df.head()


# In[13]:


x = df.drop(['Fully Paid','Term','Purpose','Home Ownership'],axis=1)


# In[15]:


res = rc.estimators_[0].decision_path([x.iloc[0]])


# In[16]:


print(rc.predict([x.iloc[0]]))


# In[17]:


from treeinterpreter import treeinterpreter as ti


# In[37]:


prediction, bias, contributions = ti.predict(rc,X_tst)
print("Prediction", prediction)
print("Bias (trainset prior)",bias)
print("Feature contributions:")
# for c, feature in zip(contributions[0], 
#                              x.columns):
#     print feature, c


# In[20]:


x.columns


# In[27]:


tst = pd.DataFrame(data=x.iloc[0])


# In[28]:


tst


# In[36]:


len(X_tst)


# In[ ]:




