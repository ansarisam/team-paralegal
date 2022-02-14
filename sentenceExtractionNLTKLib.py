#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pdfplumber
import os
import nltk
import pandas as pd


# In[2]:


nltk.download('punkt')
os.chdir('F:/Master/3rd sem/DAEN 690/CCA 2021 Q3/1st Advantage Federal Credit Union')


# In[3]:


docList = []
docDict = {}


# In[5]:


with pdfplumber.open("Mastercard Consumer Agreement.pdf") as pdf:
#Total number of pages
    totalpages = len(pdf.pages)
    for i in range(0 ,totalpages):
        pageobj = pdf.pages[i]
        #print(pageobj.extract_text())
        spageobj = str(pageobj.extract_text())
        tokens = nltk.sent_tokenize(spageobj)
        for i in range(0 ,totalpages):
            for t in tokens:
                docDict['sentence'] = t
                #print(t)
                docDictCopy = docDict.copy()
                docList.append(docDictCopy)
                #print (docDict)
print (docList)
df = pd.DataFrame(docList)
df.to_csv('F:/Master/3rd sem/DAEN 690/CCA 2021 Q3/1st Advantage Federal Credit Union/Capstone.csv', index = False, header=True)


# In[ ]:




