#!/usr/bin/env python
# coding: utf-8

# <center>
# <img src="../../img/ods_stickers.jpg" />
#     
# ## [mlcourse.ai](https://mlcourse.ai) – Open Machine Learning Course 
# Author: Arina Lopukhova (@erynn). Edited by [Yury Kashnitskiy](https://yorko.github.io) (@yorko) and Vadim Shestopalov (@vchulski). This material is subject to the terms and conditions of the [Creative Commons CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) license. Free use is permitted for any non-commercial purpose.

# # <center>Assignment #1. Fall 2019
# ## <center>Exploratory data analysis of Olympic games with Pandas
#     
# <img src='../../img/olympic_logo.png' width=50%>

# Prior to working on the assignment, you'd better check out the corresponding course material:
#  - [Exploratory data analysis with Pandas](https://nbviewer.jupyter.org/github/Yorko/mlcourse_open/blob/master/jupyter_english/topic01_pandas_data_analysis/topic1_pandas_data_analysis.ipynb?flush_cache=true), the same as an interactive web-based [Kaggle Kernel](https://www.kaggle.com/kashnitsky/topic-1-exploratory-data-analysis-with-pandas)
#  - first lectures in mlcourse.ai [YouTube playlist ](https://www.youtube.com/watch?v=QKTuw4PNOsU&list=PLVlY_7IJCMJeRfZ68eVfEcu-UcN9BbwiX) 
#  - you can also practice with demo assignments, which are simpler and already shared with solutions: [A1 demo](https://www.kaggle.com/kashnitsky/a1-demo-pandas-and-uci-adult-dataset), [solution](https://www.kaggle.com/kashnitsky/a1-demo-pandas-and-uci-adult-dataset-solution)
# 
# ### Your task is to:
#  1. write code and perform computations in the cells below
#  2. choose answers in the [webform](https://docs.google.com/forms/d/1JxhQ9Bg4OpM3E5N47ZuRbILgDuMRbvEnUbDMZK8L-NU). Solutions will be shared only with those who've filled in this form 
#  3. submit answers with some email and **remember it**! This will be your ID during the course. Specify your real full name in the form as well (no nicks allowed in the final top-100 [rating](https://mlcourse.ai/rating)). If in doubt, you can re-submit the form till the deadline for A1, no problem, but stick to only one email.
#  
# ### <center> Deadline for A1: 2019 September 15, 20:59 GMT (London time)
#     
# You'll get up to 10 credits for this assignment.
# 
# ### How to get help
# In [ODS Slack](https://opendatascience.slack.com) (if you still don't have access, fill in the [form](https://docs.google.com/forms/d/10HAN5huM996snUKjsNYyT_oOlm2uOsTKulKurb3oiNM/) mentioned on the mlcourse.ai main page), we have a channel **#mlcourse_ai_news** with announcements from the course team.
# You can discuss the course content freely in the **#mlcourse_ai** channel (we still have a huge Russian-speaking group, they have a separate channel **#mlcourse_ai_rus**).
# 
# Here's how you reply in a thread (press this dialog icon to drill down into a thread):
# 
# <img src="../../img/start_a_thread.png" />
# 
# Please stick to special threads *a1_q1-5_fall2019* and *a1_q6-10_fall2019* in **#mlcourse_ai_news** for your questions on A1. Help each other without sharing correct code and answers. Our TA **Vadim @vchulski** is there to help (only in the mentioned thread, do not write to him directly).
# 
# Lastly, you can save useful messages by pinning them, further you can find pinned items on the top, just below the channel name:
# 
# <img src="../../img/pinned_item.png" />
# 
# ### Assignment 
# __There are ten questions about 120 years of Olympic history in this task. Your task is to fill in the missing Python code and choose answers in [this web-form](https://docs.google.com/forms/d/1JxhQ9Bg4OpM3E5N47ZuRbILgDuMRbvEnUbDMZK8L-NU).__

# Download the file `athlete_events.csv` from [here](https://drive.google.com/file/d/1f5v6Z2ayc7h698FG_98wP5x1Y2zZQeox/view?usp=sharing) (scraped by [rgriffin](https://www.randigriffin.com/) from www.sports-reference.com). The dataset has the following features:
# 
# - __ID__ - Unique number for each athlete
# - __Name__ - Athlete's name
# - __Sex__ - M or F
# - __Age__ - Integer
# - __Height__ - In centimeters
# - __Weight__ - In kilograms
# - __Team__ - Team name
# - __NOC__ - National Olympic Committee 3-letter code
# - __Games__ - Year and season
# - __Year__ - Integer
# - __Season__ - Summer or Winter
# - __City__ - Host city
# - __Sport__ - Sport
# - __Event__ - Event
# - __Medal__ - Gold, Silver, Bronze, or NA

# In[1]:


import pandas as pd


# In[4]:


# Change the path to the dataset file if needed. 
PATH = r'C:\Users\Sindhuja\Desktop\ML on ML\athlete_events.csv'


# In[5]:


data = pd.read_csv(PATH)
data.head()


# __1. How old were the youngest male and female participants of the 1992 Olympics?__
# 
# *For discussions, please stick to [ODS Slack](https://opendatascience.slack.com/), channel #mlcourse_ai_news, pinned thread #a1_q1-5_fall2019*
# 
# - 16 and 15
# - 14 and 13 
# - 13 and 11
# - 11 and 12

# In[22]:


# You code here
data.sort_values('Age', inplace=True, ascending=True)
df_1992 = data[data['Year']==1992]
df_1992.sort_values('Age')


# __2. What was the percentage of male basketball players among all the male participants of the 2012 Olympics? Round the answer to the first decimal.__
# 
# *Hint:* here and further if needed drop duplicated sportsmen to count only unique ones. 
# 
# *For discussions, please stick to [ODS Slack](https://opendatascience.slack.com/), channel #mlcourse_ai_news, pinned thread #a1_q1-5_fall2019*
# 
# - 0.2
# - 1.5 
# - 2.5
# - 7.7

# In[44]:


# You code here

df_2012 = data[data['Year']==2012]
df_2012 = df_2012[df_2012['Sex']=='M']
df_2012.drop_duplicates(keep='first',subset='ID',inplace=True)
df_2012['ID'].count()


# In[53]:




df_bb_2012 = df_2012[df_2012['Sport'] == 'Basketball']
df_bb_2012['Sport'].value_counts().values
bb_m_percentage = (144/5863)*100
print(round(bb_m_percentage,1))


# __3. What are the mean and standard deviation of height for female tennis players who participated in the 2000 Olympics? Round the answer to the first decimal.__
# 
# *For discussions, please stick to [ODS Slack](https://opendatascience.slack.com/), channel #mlcourse_ai_news, pinned thread #a1_q1-5_fall2019*
# 
# - 171.8 and 6.5
# - 179.4 and 10
# - 180.7 and 6.7
# - 182.4 and 9.1 

# In[66]:


# You code here
df_2000 = data[data['Year']==2000]
df_2000 = df_2000[df_2000['Sex']=='F']


# In[75]:


df_2000.drop_duplicates(keep='first',subset='ID',inplace=True)
df_ft_2000=df_2000[df_2000['Sport']=='Tennis']
df_ft_2000.describe()


# __4. Find a sportsman who participated in the 2006 Olympics, with the highest weight among other participants of the same Olympics. What sport did he or she do?__
# 
# *For discussions, please stick to [ODS Slack](https://opendatascience.slack.com/), channel #mlcourse_ai_news, pinned thread #a1_q1-5_fall2019*
# 
# - Judo
# - Bobsleigh 
# - Skeleton
# - Boxing

# In[87]:


# You code here
df_2006 = data[data['Year']==2006]
df_weight= df_2006.drop_duplicates(keep='first',subset='ID',inplace=False)
df_weight.sort_values('Weight',ascending=False)


# __5. How many times did John Aalberg participate in the Olympics held in different years?__
# 
# *For discussions, please stick to [ODS Slack](https://opendatascience.slack.com/), channel #mlcourse_ai_news, pinned thread #a1_q1-5_fall2019*
# 
# - 0
# - 1 
# - 2
# - 3 

# In[90]:


# You code here
df_JA = data[data['Name']=='John Aalberg']
df_JA_yearly = df_JA.drop_duplicates(keep='first',subset='Year',inplace=False)
df_JA_yearly


# __6. How many gold medals in tennis did sportspeople from the Switzerland team win at the 2008 Olympics? Count every medal from every sportsperson.__
# 
# *For discussions, please stick to [ODS Slack](https://opendatascience.slack.com/), channel #mlcourse_ai_news, pinned thread #a1_q6-10_fall2019*
# 
# - 0
# - 1 
# - 2
# - 3 

# In[94]:


# You code here
df_SWT = data[data['Team']=='Switzerland']
df_SWT = df_SWT[df_SWT['Year']==2008]
df_SWT = df_SWT[df_SWT['Sport']=='Tennis']
df_SWT =  df_SWT[df_SWT['Medal']=='Gold']
df_SWT


# __7. Is it true that Spain won fewer medals than Italy at the 2016 Olympics? Do not consider NaN values in _Medal_ column.__ 
# 
# *For discussions, please stick to [ODS Slack](https://opendatascience.slack.com/), channel #mlcourse_ai_news, pinned thread #a1_q6-10_fall2019*
# 
# - Yes
# - No

# In[112]:


# You code here
df_CMP = data[data['Year']==2016]
df_Spain = df_CMP[df_CMP['Team']=='Spain']
df_Italy = df_CMP[df_CMP['Team']=='Italy']
df_Spain = df_Spain[df_Spain['Medal']=='Gold']
df_Spain
len(df_Spain)


# In[113]:


df_Italy = df_Italy[df_Italy['Medal']=='Gold']
len(df_Italy)


# __8. What age category did the fewest and the most participants of the 2008 Olympics belong to?__
# 
# *For discussions, please stick to [ODS Slack](https://opendatascience.slack.com/), channel #mlcourse_ai_news, pinned thread #a1_q6-10_fall2019*
# 
# - [45-55] and [25-35) correspondingly
# - [45-55] and [15-25) correspondingly
# - [35-45) and [25-35) correspondingly
# - [45-55] and [35-45) correspondingly

# In[127]:


# You code here
df_Y_CMP = data[data['Year']==2008]
df_Y_CMP1 = df_Y_CMP[df_Y_CMP['Age'].between(45,55)]
df_Y_CMP2 = df_Y_CMP[df_Y_CMP['Age'].between(25,35)]
df_Y_CMP3 = df_Y_CMP[df_Y_CMP['Age'].between(15,25)]
df_Y_CMP4 = df_Y_CMP[df_Y_CMP['Age'].between(35,45)]
print(len(df_Y_CMP1),len(df_Y_CMP2),len(df_Y_CMP3),len(df_Y_CMP4))


# __9. Is it true that there were Summer Olympics held in Atlanta? Is it true that there were Winter Olympics held in Squaw Valley?__
# 
# *For discussions, please stick to [ODS Slack](https://opendatascience.slack.com/), channel #mlcourse_ai_news, pinned thread #a1_q6-10_fall2019*
# 
# - Yes, Yes
# - Yes, No
# - No, Yes 
# - No, No 

# In[107]:


# You code here
df_Sum_City = data[data['Season']=='Summer']
df_Win_City = data[data['Season']=='Winter']
df_Sum_CityL = df_Sum_City['City'].drop_duplicates(keep='first',inplace=False)
df_Sum_CityL


# In[108]:


df_Win_CityL = df_Win_City['City'].drop_duplicates(keep='first',inplace=False)
df_Win_CityL


# __10. What is the absolute difference between the number of unique sports at the 1986 Olympics and 2002 Olympics?__
# 
# *For discussions, please stick to [ODS Slack](https://opendatascience.slack.com/), channel #mlcourse_ai_news, pinned thread #a1_q6-10_fall2019*
# 
# - 3 
# - 10
# - 15
# - 27 

# In[119]:


# You code here
df_1986 = data[data['Year']==1986]
df_2002 = data[data['Year']==2002]
df_2k2_spr = df_2002['Sport'].drop_duplicates(keep='first',inplace=False)
len(df_2k2_spr)


# In[120]:


df_2k2_spr


# That's it! Now go and do 30 push-ups! :)
