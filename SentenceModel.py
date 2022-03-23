#!/usr/bin/env python
# coding: utf-8

# In[83]:


from datasets import load_dataset
import datasets
from transformers import AutoTokenizer, DataCollatorWithPadding
import pandas as pd
checkpoint = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)


# In[84]:


dataset = load_dataset('csv', data_files={'train': ['train.csv'], 'test': 'test.csv', 'validation':'validation.csv'})


# In[85]:


def tokenize_function(example):
    try:
      return tokenizer(example["text"], truncation=True)
    except  Exception as e:
      print(e)


# In[86]:


tokenized_datasets = dataset.map(tokenize_function, batched=True)
print("tokenized_datasets::", tokenized_datasets)
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)


# In[87]:


from transformers import TrainingArguments

training_args = TrainingArguments(output_dir="test_trainer")


# In[88]:


from transformers import AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained(checkpoint, num_labels=4)


# In[89]:


from transformers import Trainer

trainer = Trainer(
    model,
    training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation"],
    data_collator=data_collator,
    tokenizer=tokenizer,
)


# In[90]:


trainer.train()


# In[99]:


from transformers import pipeline

classifier = pipeline(task = 'text-classification', model = 'bert-base-uncased', tokenizer=tokenizer)


# In[100]:


classifier(["Your Zions First National Bank Card has been issued by Zions Bancorporation, NA dba Zions First National Bank.", "Your Account is with Zions Bancorporation, NA (Bank) and will be administered by the Banks Bankcard Services department.", "Your Credit Card, monthly statement, and other associated materials will bear the Zions First National Bank, National Bank of Arizona, Nevada State Bank, or Vectra Bank Colorado name.", "The Card is the property of the Bank."])


# In[ ]:




