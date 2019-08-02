#!/usr/bin/env python
# coding: utf-8

# In[223]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn 
from sklearn.linear_model import LinearRegression
import os
datapath = os.path.join("datasets", "lifesat", "")


# In[224]:


bli = pd.read_csv(r"C:/Users/Sindhuja/Data/BLI_01082019132123935.csv", thousands=',',encoding='latin')
oecd_bli = pd.read_csv(r"C:/Users/Sindhuja/Data/BLI_01082019132123935.csv")
oecd_bli.to_csv(r"C:/Users/Sindhuja/Data/BLI_01082019132123935.csv", encoding='utf-8')
oecd_bli.head()


# In[225]:


gdp_file = r'C:\Users\Sindhuja\Data\GDPEXCEL.xls'
gdp_per_capita = pd.read_excel(gdp_file)
gdp_per_capita.head()


# In[242]:


oecd_bli = oecd_bli[oecd_bli["INEQUALITY"]=="TOT"]
oecd_bli = oecd_bli[oecd_bli["Indicator"]=="Life satisfaction"]
#oecd_bli.to_csv(r"C:/Users/Sindhuja/Data/TOT.csv")
df_gdp = gdp_per_capita[['Country',2015]]
df_inx = oecd_bli[['Country','Value']]


# In[244]:


country_stats = pd.merge(df_inx, df_gdp, on='Country', how='left')


# In[245]:


country_stats[['Value']].head


# In[246]:


country_stats.plot(kind='scatter', x=2015, y='Value')
plt.show()


# In[248]:


model= sklearn.linear_model.LinearRegression()


# In[249]:


X = np.c_[country_stats[2015]]
y = np.c_[country_stats['Value']]
model.fit(X,y)


# In[250]:


X_new=[[22960]]


# In[251]:


print(model.predict(X_new))


# In[ ]:




