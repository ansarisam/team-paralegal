#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pdfplumber
import os
import nltk
import pandas as pd


# In[8]:


nltk.download('punkt')
os.chdir('F:/Master/3rd sem/DAEN 690/CCA 2021 Q3/1st Advantage Federal Credit Union')
path_of_directory = 'F:/Master/3rd sem/DAEN 690/CCA 2021 Q3/1st Advantage Federal Credit Union'
ext = ('.pdf')


# In[9]:


docList = []
docDict = {}


# In[10]:


for files in os.listdir(path_of_directory):
    if files.endswith(ext):
        with pdfplumber.open(files) as pdf:
        #Total number of pages
            totalpages = len(pdf.pages)
            for i in range(0 ,totalpages):
                pageobj = pdf.pages[i]
                #print(pageobj.extract_text())
                spageobj = str(pageobj.extract_text())
                tokens = nltk.sent_tokenize(spageobj)
                for t in tokens:
                    docDict['File Name'] = files
                    docDict['Sentence'] = t
                    docDict['Labels'] = 0
                    #print(t)
                    docDictCopy = docDict.copy()
                    docList.append(docDictCopy)
                    #print (docDict)


# In[11]:


df = pd.DataFrame(docList)
df.to_csv('F:/Master/3rd sem/DAEN 690/CCA 2021 Q3/1st Advantage Federal Credit Union/Capstone.csv', index = False, header=True)


# In[ ]:




