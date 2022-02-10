#!/usr/bin/env python
# coding: utf-8

# In[37]:


#from tika import parser
import pdfplumber
import os
os.chdir('F:/Master/3rd sem/DAEN 690/CCA 2021 Q3/1st Advantage Federal Credit Union')


# In[36]:


with pdfplumber.open("Mastercard Consumer Agreement.pdf") as pdf:
#Total number of pages
    totalpages = len(pdf.pages)
    for i in range(0 ,totalpages):
        pageobj = pdf.pages[i]
        print(pageobj.extract_text())
        
    #loop end
#big loop end


# In[ ]:




