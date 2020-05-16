#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()


# In[2]:


agent=pd.read_csv('Agents.csv')


# In[3]:


agent.head(4)


# In[4]:


agent.shape


# In[5]:


#Checked if there is any duplicated columns
agent.duplicated().sum()


# In[6]:


#Infomation about the dataframe
agent.info()


# In[7]:


#types of the data in which there are encoded
agent.dtypes


# In[8]:


#Checking statistical values of our dataset
agent.describe()


# In[9]:


#Converting the TransactionDate to datetime
agent['TransactionDate']=pd.to_datetime(agent['TransactionDate'])
agent['AccountOpenedDate']=pd.to_datetime(agent['AccountOpenedDate'])


# In[10]:


agent.dtypes


# ## Basic EDA

# In[11]:


'''
Performed a grouby to assigned each Agent to it total amount of transaction done'''
agent_groub=agent.groupby(by=agent['FullName'])
x=np.round(agent_groub.sum()['TransactionAmount'])
agent['total_amount']=agent['FullName'].map(x)


# In[12]:


#Each Transaction has a unique agent
agent.total_amount.nunique() - agent.FullName.nunique()


# In[13]:



agent[agent.total_amount==299944121].head(5)


# In[14]:


agent_top_10=agent.groupby('FullName').sum().sort_values(by='TransactionAmount', ascending=False).head(10)
plt.figure(figsize=(10,8))
plt.xlabel('Full Name')
plt.ylabel('Transaction Amount')
plt.xticks(rotation=20)
plt.title('Transaction Amount by Agent Since Inception of Company')
plt.plot(agent_top_10['TransactionAmount'], color='red', marker='+', linestyle=':')
plt.show();


# ## Highest Sale in 2019

# In[15]:


#create a column for the month column
agent['month']=agent['TransactionDate'].dt.month
agent['year']=agent['TransactionDate'].dt.year


# In[16]:


#Looping through the month column to form a new column quarter in the dataset
quarter=[]
for i in agent['month']:
    if i==1 or i==2 or i==3:
        quarter.append(1)
    elif i==4 or i==5 or i==6:
        quarter.append(2)
    elif i==7 or i==8 or i==9:
        quarter.append(3)
    elif i==10 or i==11 or i==12:
        quarter.append(4)
agent['quarters']=quarter
        


# In[17]:


agent_2019_quarter4=agent[(agent['year']==2019) & (agent['quarters']==4)]


# In[18]:


agent_quarter_top_10=agent_2019_quarter4.groupby('FullName').sum().sort_values(by='TransactionAmount', ascending=False).head(10)
plt.figure(figsize=(10,8))
plt.xlabel('Full Name')
plt.ylabel('Transaction Amount')
plt.xticks(rotation=30)
plt.title('Transaction For 2019')
plt.plot(agent_quarter_top_10['TransactionAmount'],color='green', marker='o', linestyle='dashed')
plt.show();


# ## Agent Raj Verma

# In[19]:


agent_raj_verma=agent[agent['FullName']=='Raj Verma']
print('Shape of the dataset',agent_raj_verma.shape)
agent_raj_verma.head(4)


# In[20]:


agent_sum=agent_raj_verma[agent_raj_verma['year']==2020]['TransactionAmount'].sum()
agent_sum=np.round(agent_sum/1000000, decimals=2)
print('Total Amount of Transaction Carried out by Agent Raj Verma for the First Quater of 2020:',agent_sum,'Million')


# In[21]:


quarter_1=agent_raj_verma[(agent_raj_verma['year']==2019) &(agent_raj_verma['quarters']==1)]['TransactionAmount'].sum()
quarter_2=agent_raj_verma[(agent_raj_verma['year']==2019) &(agent_raj_verma['quarters']==2)]['TransactionAmount'].sum()
quarter_3=agent_raj_verma[(agent_raj_verma['year']==2019) &(agent_raj_verma['quarters']==3)]['TransactionAmount'].sum()
quarter_4=agent_raj_verma[(agent_raj_verma['year']==2019) &(agent_raj_verma['quarters']==4)]['TransactionAmount'].sum()

(quarter_1, quarter_2, quarter_3, quarter_4)=np.round(quarter_1/1000000, decimals=2),np.round(quarter_2/1000000, decimals=2),np.round(quarter_3/1000000, decimals=2),np.round(quarter_4/1000000, decimals=2)

print(f'Transaction for quarter 1 {quarter_1}Million')
print(f'Transaction for quarter 2 {quarter_2}Million')
print(f'Transaction for quarter 3 {quarter_3}Million')
print(f'Transaction for quarter 4 {quarter_4}Million')


# In[22]:


#Created a new dataframe for the quarter columns
quarter_data={'Quarter':['Quarter 1', 'Quarter 2', 'Quarter 3', 'Quarter 4'], 'Amount in Million':[19.67, 16.15, 15.29, 5.38]}
quarter_data=pd.DataFrame(quarter_data)


# In[23]:


quarter_data.plot(x='Quarter', y='Amount in Million', kind='bar',
                  legend=True,title='Transaction by Quarter of Agent Raj Virma');


# In[ ]:





# In[ ]:





# # SUPPLIER EVALUATION

# In[24]:


supplier=pd.read_csv('DSuppliers.csv')


# In[25]:


supplier.head(4)


# In[26]:


#Checked if there is any duplicated columns
supplier.duplicated().sum()


# In[27]:


supplier.shape


# In[28]:


supplier.info()


# In[29]:


supplier.dtypes


# In[30]:


#Checking statistical values of our dataset
supplier.describe()


# In[31]:


#Checking for the total number of supplier Name of all products
print('Number of Suppliers:',supplier.SupplierName.nunique())
supplier.SupplierName.value_counts()


# In[32]:


#Checking for the total number of products
print('Number of Unique Products:',supplier.SupplierCategoryName.nunique())
supplier.SupplierCategoryName.value_counts()


# In[33]:


supplier_name=supplier.groupby('SupplierName').sum().sort_values(by='TransactionAmount', ascending=False)
supplier_name


# In[34]:


plt.figure(figsize=(10,8))
plt.xlabel('Full Name')
plt.ylabel('Transaction Amount')
plt.xticks(rotation=30)
#plt.legend()
plt.title('Transaction Amount of Supplies')
plt.plot(supplier_name['TransactionAmount'],color='pink', marker='*', linestyle='dashed')
plt.show();


# In[35]:


total_amt=(supplier.TransactionAmount.sum())/1000000000
total_amt=np.round(total_amt, decimals=2)
print('Total Money Spent on supplies:',total_amt,'Billion')


# In[36]:


agent.to_csv('Agents_new.csv')


# In[ ]:





# ## I hope it is comprehensive Enough 

# In[ ]:




