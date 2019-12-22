#!/usr/bin/env python
# coding: utf-8

# In[12]:


alpha='abcdefghijklmnopqrstuvwxyz'
l1=input("Enter your message:")
key=int(input("Enter your key:"))
n=len(l1)
l2=""
for i in range(n):
    ch=l1[i]
    location=alpha.find(ch)
    new_location=(location+key)%26
    l2+=alpha[new_location]
    
  
print(l2)
    


# In[ ]:





# In[ ]:




