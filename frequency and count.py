#!/usr/bin/env python
# coding: utf-8

# In[10]:


str=input("Enter string:")
str=str.split()
s=[]
for i in str:
    if i not  in s:
         s.append(i)
for i in range(0,len(s)):
    print('Frequency of',s[i],'is:',str.count(s[i]))

    
        
        
    

