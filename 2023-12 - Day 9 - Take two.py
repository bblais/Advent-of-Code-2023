#!/usr/bin/env python
# coding: utf-8

# ![image.png](attachment:f3b13bfc-12fe-47bb-94d5-9446e301dc59.png)
# ![image.png](attachment:6f1b3d2a-4d2b-4a28-9093-62d71957a027.png)

# In[15]:


from numpy import array,polyfit,diff,arange,polyval,round,sum,prod,cumsum


# In[11]:


seq=[1,   3,   6,  10,  15,  21]


# In[12]:


seq=array(seq)


# In[13]:


seq_tower=[seq]
while not all(seq_tower[-1]==0):
    seq_tower.append(diff(seq_tower[-1]))
seq_tower


# In[14]:


[seq[-1] for seq in seq_tower][::-1]


# In[16]:


cumsum([seq[-1] for seq in seq_tower][::-1])


# In[17]:


def predict_next_val(seq):
    seq_tower=[seq]
    while not all(seq_tower[-1]==0):
        seq_tower.append(diff(seq_tower[-1]))

    val=cumsum([seq[-1] for seq in seq_tower][::-1])[-1]
    return val    


# In[26]:


S="""
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""".strip()
lines=S.split('\n')
seqs=[]
for line in lines:
    if not line:
        continue
    seq=array([int(_) for _ in line.split()])
    seqs.append(seq)
seqs


# In[19]:


vals=[predict_next_val(seq) for seq in seqs]
print(sum(vals))


# In[27]:


S=open('data/day9.txt').read()
lines=S.split('\n')
print(len(lines))
seqs=[]
for line in lines:
    if not line:
        continue
    
    seq=array([int(_) for _ in line.split()])
    seqs.append(seq)


# In[29]:


vals=[]
for i,seq in enumerate(seqs):
    vals.append(predict_next_val(seq))
print(sum(vals))
    


# In[25]:


line


# In[ ]:




