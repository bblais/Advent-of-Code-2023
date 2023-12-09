#!/usr/bin/env python
# coding: utf-8

# In[2]:


S="""
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
""".strip()

lines=S.split("\n")
instructions=lines[0]
print(instructions)


# In[3]:


D={}
for line in lines[2:]:

    key=line.split("=")[0].strip()
    L=line.split("(")[1].split(",")[0].strip()
    R=line.split("(")[1].split(",")[1].split(")")[0].strip()

    D[key]={'L':L,'R':R}


# In[4]:


D


# In[5]:


key='AAA'
count=0
while key!='ZZZ':
    inst=instructions[count % len(instructions)]
    print(key," ",inst,"-->",D[key][inst])
    key=D[key][inst]
    count+=1
    if count>20:
        break
print(count)


# In[6]:


S="""
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
""".strip()
lines=S.split("\n")
instructions=lines[0]
print(instructions)


# In[7]:


D={}
for line in lines[2:]:

    key=line.split("=")[0].strip()
    L=line.split("(")[1].split(",")[0].strip()
    R=line.split("(")[1].split(",")[1].split(")")[0].strip()

    D[key]={'L':L,'R':R}


# In[8]:


key='AAA'
count=0
while key!='ZZZ':
    inst=instructions[count % len(instructions)]
    print(key," ",inst,"-->",D[key][inst])
    key=D[key][inst]
    count+=1
    if count>20:
        break

print(count)


# In[24]:


S=open('data/day8.txt').read().strip()
lines=S.split("\n")
instructions=lines[0]
print(instructions)


# In[25]:


D={}
for line in lines[2:]:

    key=line.split("=")[0].strip()
    L=line.split("(")[1].split(",")[0].strip()
    R=line.split("(")[1].split(",")[1].split(")")[0].strip()

    D[key]={'L':L,'R':R}


# In[26]:


key='AAA'
count=0
while key!='ZZZ':
    inst=instructions[count % len(instructions)]
    key=D[key][inst]
    count+=1

print(count)


# In[ ]:





# In[27]:


keys=list(D.keys())
keys=[key for key in keys if key.endswith('A')]
len(keys)


# In[28]:


all([key.endswith('A') for key in keys])


# In[29]:


import sys


# In[30]:


count=0
while True:
    inst=instructions[count % len(instructions)]
    keys=[D[key][inst] for key in keys]
    count+=1

    if all([key.endswith('Z') for key in keys]):
        break

    if count%1000000 ==0:
        print(".",end="")
        sys.stdout.flush()
print(count)


# In[31]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *


# In[40]:


keys=list(D.keys())
keys=[key for key in keys if key.endswith('A')]

count=0
data={}
for i,key in enumerate(keys):
        data[i]=[]
    
while True:
    inst=instructions[count % len(instructions)]
    keys=[D[key][inst] for key in keys]
    count+=1

    if all([key.endswith('Z') for key in keys]):
        break

    for i,key in enumerate(keys):
        if key.endswith('Z'):
            data[i].append(count)

    if count>100000:
        break

print(count)


# In[43]:


for key in data:
    plot(data[key],'o')


# In[ ]:




