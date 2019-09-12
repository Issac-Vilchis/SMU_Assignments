#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import dependencies
import pandas as pd


# In[2]:


#load and read the budget.csv file
election_csv=r'C:\Users\Owner\Desktop\SMU_Assignments\Unit_03_Python\Instructions\PyPoll\Resources\election_data.csv'
print(election_csv)


# In[3]:


#Read csv to dataframe
election_df=pd.read_csv(election_csv,encoding="ISO-8859-1")
election_df.head()


# In[4]:


#The total number of votes cast
vote_count=election_df["Voter ID"].count()
vote_count


# In[5]:


#A complete list of candidates who received votes
print("The total number of votes each candidate won\n",election_df["Candidate"].value_counts())


# In[6]:


#The percentage of votes each candidate won
#print(election_df["Candidate"].value_counts()/vote_count)
print("The percentage of votes each candidate won \n", election_df["Candidate"].value_counts()/vote_count * 100)


# In[7]:


print("The total number of votes each candidate won\n",election_df["Candidate"].value_counts())

find_winner = election_df["Candidate"].value_counts()
print(find_winner.head(1))




#%%
