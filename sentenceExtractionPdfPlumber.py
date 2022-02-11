#!/usr/bin/env python
# coding: utf-8

# In[1]:


#from tika import parser
import pdfplumber
import csv
import pandas as pd
import spacy
nlp = spacy.load('en_core_web_sm')
import os
os.chdir('F:/Master/3rd sem/DAEN 690/CCA 2021 Q3/1st Advantage Federal Credit Union')


# In[2]:


pdf_path = "Mastercard Consumer Agreement.pdf"
#csv_path = "Mastercard Consumer Agreement.csv"


# In[3]:


def extract_text_data(path):
    text = ""
    try:
        with pdfplumber.open(path) as pdf:
            for i in pdf.pages:
                text += i.extract_text()
            return text
    except:
        return None

extracted_text = extract_text_data(pdf_path)

#print(extracted_text)


# In[4]:


def extract_sentence(extracted_text):
    nlp_text = nlp(extracted_text)
    

    # Sentence Tokenizer
    nlp_text = [sent.text.strip() for sent in nlp_text.sents]
    
    for sentence in nlp_text:
        print (sentence)
        
              


# In[126]:


def export_to_csv(pdf_path, csv_path):
    
    with open(csv_path, 'w') as csv_file:
        writer = csv.writer(csv_file)
        for i in extract_sentence(extracted_text):
            writer.writerow(i)


# In[127]:


export_to_csv(pdf_path, csv_path)


# In[5]:


extract_sentence(extracted_text)


# In[ ]:




