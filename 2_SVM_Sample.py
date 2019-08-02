#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np

from sklearn import svm, datasets
import matplotlib.pyplot as plt


# In[19]:


iris = datasets.load_iris()
X = iris.data[:,:2]
y = iris.target
x_min, x_max = X[:,0].min()-1,X[:,0].max()+1
y_min, y_max = X[:,1].min()-1,X[:,1].max()+1
h = (x_max/x_min)/100
xx, yy = np.meshgrid(np.arange(x_min, x_max,h), np.arange(y_min,y_max,h))
X_plot = np.c_[xx.ravel(),yy.ravel()]
C = 1.0


# In[22]:


svc_classifier = svm.SVC(kernel='linear', C=C, decision_function_shape = 'ovr').fit(X,y)


# In[31]:


Z = svc_classifier.predict(X_plot)
Z = Z.reshape(xx.shape)
plt.figure(figsize =(15,5))
plt.subplot(121)
plt.contourf(xx,yy,Z,cmap = plt.cm.tab10, alpha = 0.3)
plt.scatter(X[:,0],X[:,1],c=y,cmap = plt.cm.Set1)
plt.xlabel("Sepal length")
plt.ylabel("Sepal Width")
plt.xlim(xx.min(),xx.max())
plt.title('SVC with linear Kernel')


# In[30]:


plt.scatter(X[:,0],X[:,1],c=y,cmap = plt.cm.Set1)
plt.xlabel("Sepal length")
plt.ylabel("Sepal Width")
plt.xlim(xx.min(),xx.max())
plt.title('SVC with linear Kernel')

