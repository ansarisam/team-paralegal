#!/usr/bin/env python
# coding: utf-8

# In[17]:


path = 'C:\DAEN_690\Credit_Card_Agreements_2021_Q3\CCA 2021 Q3'
total_pdfs = 0
total_banks = 0

for base, banks, pdfs in os.walk(path):
    for each_bank in banks:
        total_banks += 1
    for each_pdf in pdfs:
        total_pdfs += 1

print("Total number of documents (pdf's):",total_pdfs)
print('Total Number of Banks:',total_banks)

