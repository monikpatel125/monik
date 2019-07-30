#!/usr/bin/env python
# coding: utf-8

# In[19]:


import math as m
l=input("Enter numbers with comma:")
l=l.split(',')
l1=[]
for i in l:
    l1.append(int(i))
c=50
h=30
l2=[]
for d in l1:
    q=m.sqrt((2*c*d)/h)
    l2.append(int(q))
print(l2)
    

