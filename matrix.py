#!/usr/bin/env python
# coding: utf-8

# In[2]:


x=int(input("enter row:"))
y=int(input("enter col:"))
def a(x,y):
    l=[i*j for j in range(y) for i in range(x)]
    return l
print(a(y,x))

