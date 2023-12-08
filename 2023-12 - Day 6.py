#!/usr/bin/env python
# coding: utf-8

# https://adventofcode.com/2023/day/6

# In[1]:


S="""
Time:      7  15   30
Distance:  9  40  200
""".strip()
lines=S.split('\n')


# In[2]:


time=[int(_) for _ in lines[0].split()[1:]]
distance=[int(_) for _ in lines[1].split()[1:]]


# In[3]:


time,distance


# In[4]:


t=7
d=9


# In[5]:


def D(hold,t=7):
    v=hold
    to=hold
    return (t-to)*v


# In[8]:


from numpy import arange


# In[7]:


D(2,t=7)


# In[16]:


total=1
for t,d in zip(time,distance):
    total*=(D(arange(t+1),t=t)>d).sum()
total


# In[17]:


S=open('data/day6.txt').read().strip()
lines=S.split('\n')
len(lines)


# In[18]:


time=[int(_) for _ in lines[0].split()[1:]]
distance=[int(_) for _ in lines[1].split()[1:]]


# In[19]:


total=1
for t,d in zip(time,distance):
    total*=(D(arange(t+1),t=t)>d).sum()
total


# ## Part 2

# In[20]:


S="""
Time:      7  15   30
Distance:  9  40  200
""".strip()
lines=S.split('\n')


# In[21]:


time=int("".join(lines[0].split()[1:]))
distance=int("".join(lines[1].split()[1:]))
time,distance


# In[22]:


t=time
d=distance
(D(arange(t+1),t=t)>d).sum()


# In[23]:


S=open('data/day6.txt').read().strip()
lines=S.split('\n')
len(lines)


# In[24]:


time=int("".join(lines[0].split()[1:]))
distance=int("".join(lines[1].split()[1:]))
time,distance


# In[25]:


t=time
d=distance
(D(arange(t+1),t=t)>d).sum()


# In[ ]:




