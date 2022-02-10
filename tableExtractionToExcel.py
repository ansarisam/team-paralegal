#!/usr/bin/env python
# coding: utf-8

# In[33]:


import os
import tabula
os.chdir('F:/Master/3rd sem/DAEN 690/CCA 2021 Q3/1st Advantage Federal Credit Union')


# In[34]:


tables = tabula.read_pdf("Mastercard Consumer Disclosure.pdf", pages="all")


# In[35]:


folder_name = "tables"
if not os.path.isdir(folder_name):
    os.mkdir(folder_name)
# iterate over extracted tables and export as excel individually
for i, table in enumerate(tables, start=1):
    table.to_excel(os.path.join(folder_name, f"table_{i}.xlsx"), index=False)


# In[ ]:




