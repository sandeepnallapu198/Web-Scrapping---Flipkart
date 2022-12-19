#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing libraries

from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


# In[54]:


link = 'https://www.flipkart.com/samsung-galaxy-f22-denim-blue-64-gb/p/itmce0a6baf0d54d?pid=MOBG43UGBTGGB99V&lid=LSTMOBG43UGBTGGB99VLZACSD&marketplace=FLIPKART&q=mobiles&store=tyy%2F4io&srno=s_1_2&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&fm=neo%2Fmerchandising&iid=019cb908-5844-4f1a-9a9a-27055b7118ba.MOBG43UGBTGGB99V.SEARCH&ppt=browse&ppn=browse&ssid=bvs86fmz5c0000001671249046071&qH=eb4af0bf07c16429'


# In[55]:


page = requests.get(link)


# In[56]:


page


# In[57]:


page.content


# In[58]:


soup = bs(page.content,'html.parser')
print(soup.prettify)


# In[59]:


names = names=soup.find_all('p', class_="_2sc7ZR _2V5EHH")
names


# In[60]:


cust_names = []
for i in range(len(names)):
    cust_names.append(names[i].get_text())


# In[61]:


cust_names


# In[62]:


reviews = soup.find_all('p', class_="_2-N8zT")
reviews


# In[63]:


Reviews = []
for i in range(len(reviews)):
    Reviews.append(reviews[i].get_text())


# In[64]:


Reviews


# In[65]:


df = pd.DataFrame()


# In[66]:


df['NAMES'] = cust_names
df['REVIEWS'] = Reviews


# In[67]:


df


# In[75]:


df.to_csv('E:\Flipkart WebScrapping Project.csv',index = False)


# In[ ]:




