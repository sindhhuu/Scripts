#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sklearn


# In[4]:


from sklearn.datasets import load_breast_cancer


# In[5]:


data = load_breast_cancer()


# In[6]:


data['target_names']


# In[9]:


label_names = data['target_names']


# In[10]:


labels = data['target']
feature_names = data['feature_names']
features = data['data']


# In[12]:


print (labels)


# In[13]:


print(features[0])


# In[15]:


print(feature_names[0])


# In[16]:


from sklearn.model_selection import train_test_split


# In[32]:


train, test, train_labels, test_labels = train_test_split(features,labels,test_size=0.40,random_state=60)


# In[33]:


from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
model=gnb.fit(train, train_labels)


# In[34]:


predictions = gnb.predict(test)


# In[35]:


print(predictions)


# In[36]:


from sklearn.metrics import accuracy_score
print (accuracy_score(test_labels,predictions))


# In[ ]:




