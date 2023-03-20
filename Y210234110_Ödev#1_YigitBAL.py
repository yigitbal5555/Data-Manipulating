#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


import numpy as np


# In[4]:


import csv


# In[5]:


data1 = pd.read_csv('scopus.csv')


# In[6]:


data2 = pd.read_csv('csv-Machinelea-set.csv')


# In[7]:


data1.shape


# In[8]:


data2.shape


# In[10]:


data1.sample(4)


# In[11]:


data2.sample(4)


# In[12]:


data1.describe()


# In[13]:


data2.describe()


# In[19]:


data2.nunique()


# In[23]:


data1.nunique()


# In[26]:


data2.columns


# In[27]:


data1.columns


# In[90]:


df1 = data1[[''Authors', 'Author(s) ID', 'Title', 'Year', 'Source title', 'Volume',
       'Issue', 'Art. No.', 'Page start', 'Page end', 'Page count', 'Cited by',
       'DOI', 'Link', 'Affiliations', 'Authors with affiliations',
       'Author Keywords', 'Index Keywords', 'Publisher', 'PubMed ID]]


# In[55]:


df2 = data2[['PMID', 'Title', 'Authors', 'Citation', 'First Author', 'Journal/Book',
       'Publication Year', 'Create Date', 'PMCID', 'NIHMS ID', 'DOI']]


# In[39]:


df1['Document Type'].unique()


# In[48]:





# In[65]:


df1.isna().sum()


# In[64]:


df2.isna().sum()


# In[67]:


df1['DOI'].isin(df2['DOI']).value_counts()


# In[71]:


df1[pd.isnull(df1['DOI'])==True]


# In[ ]:





# In[72]:


df2[pd.isnull(df2['DOI'])==True]


# In[ ]:


#Hocam Burada, df2'nin DOI olan satırları sıfır (0) gelmektedir.


# In[ ]:


#df2'de yani scopus'ta DOI bilgisi ilginç şekilde 0 (Sıfır) geldi, 
#bunu da değiştiremedim, kendim manuel olarak veri setine DOI eklemeye çalıştım ama olmadı.
#bu yüzden de df1 ve df2'nin kesişimini çıkartamadım,
#çünkü df2'de sıfır geldiği için ortaklıkları bulunmuyor maalesef.


# In[ ]:


#bu sebeple scopus değil de pubmed'de DOI olanları çıakrtacağım.


# In[ ]:


#2021 6th International Conference on Image Inf...


# In[73]:


df1[df1['Title'].str.contains('2021 6th International Conference on Image Inf')]


# In[74]:


df1[df1['Title'].str.contains('21st IEEE International Symposium on Computati')]


# In[76]:


df1[df1['Title'].str.contains('Category boosting machine learning algorithm f')]


# In[77]:


df1[df1['Title'].str.contains('Advanced imaging of gliomas')]


# In[78]:


df1[df1['Title'].str.contains('A multi-omics-based serial deep learning appro')]


# In[79]:


df1[df1['Title'].str.contains('Identification and validation of significant g')]


# In[80]:


df1[df1['Title'].str.contains('The diagnostic accuracy of convolutional neura')]


# In[97]:


titlesdf2 = df2[pd.isnull(df2['DOI'])=='True']['Title']


# In[98]:


titlesdf1 = df1[pd.isnull(df1['DOI'])=='True']['Title']


# In[99]:


df1[df1['Title'].str.contains('12th International Conference on Bioinformatic...')]


# In[108]:


for num,tit in zip(titlesdf2.index,titlesdf2.values):
    if len(df1[df1['Title'].str.contains(tit)])


# In[ ]:


#Burada hatayı düzeltemedimi neden hata verdiğini de anlayamadım. :/ 


# In[109]:


df2.loc[124,['DOI']]


# In[125]:


df1.loc[124,['DOI']]


# In[ ]:


#10.1002/ejhf.2361


# In[126]:


df2.loc[124,['DOI']]='10.1002/ejhf.2361'


# In[127]:


len(df1[pd.isnull(df1['DOI'])==True])


# In[141]:


#df2_Drop = df2.drop(['DOI'], axis=1)


# In[142]:


#df1_Drop = df1.drop(['DOI'], axis=1)


# In[143]:


df2_Drop.columns


# In[144]:


df1_Drop.columns


# In[158]:


Union_Df2_Drop = df2_Drop[['Title','Authors','Publication Year','DOI']]


# In[157]:


Union_Df1_Drop = df1_Drop[['Authors','Title','Year','DOI']]


# In[147]:


Union_Them_All = Union_Df1_Drop.append(Union_Df2_Drop)


# In[148]:


#Hepsinin ( Tüm Union'ların birleştirilmesi için Union Them ALL Tanımlandı.)


# In[149]:


Union_Them_All


# In[155]:


Union_Them_All_Without_Duplicates=Union_Them_All.drop_duplicates(subset='DOI',keep='first',inplace=False,ignore_index=True)


# In[159]:


Union_Them_All_Without_Duplicates.shape


# In[165]:


merge_PPI = Union_Them_All.loc[(Union_Them_All['Title'].str.contains('Activity'))]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




