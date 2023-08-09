#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')


# In[3]:


print(soup)


# In[4]:


soup.find_all('table')[1]


# In[23]:


soup.find('table', class_ = 'wikitable sortable')


# In[24]:


table = soup.find_all('table')[1]
print(table)


# In[26]:


world_titles = table.find_all('th')


# In[27]:


world_table_titles = [title.text.strip() for title in world_titles]
print(world_table_titles)


# In[33]:


pip install --upgrade pip


# In[35]:


pip install jupyter


# In[36]:


get_ipython().system('pip install pandas')


# In[39]:


import pandas as pd


# In[41]:


df = pd.DataFrame(columns = world_table_titles)
df


# In[42]:


column_data = table.find_all('tr')


# In[46]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data
    


# In[47]:


df


# In[49]:


df.to_csv(r'C:\Users\ADMIN\OneDrive\Documents\web_scrapping\companies.csv', index = False)


# In[ ]:




