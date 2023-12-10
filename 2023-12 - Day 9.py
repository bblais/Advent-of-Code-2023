#!/usr/bin/env python
# coding: utf-8

# ![image.png](attachment:f3b13bfc-12fe-47bb-94d5-9446e301dc59.png)
# ![image.png](attachment:6f1b3d2a-4d2b-4a28-9093-62d71957a027.png)

# In[2]:


from numpy import array,polyfit,diff,arange,polyval,round,sum,prod


# In[3]:


# from https://www.foster77.co.uk/Foster,%20Mathematics%20In%20School,%20Differences%20Over%20Differences%20Methods.pdf

seq=[8, 15, 24, 35, 48]


# In[4]:


seq=array(seq)


# In[5]:


def get_power(seq):
    dseq=seq
    count=0
    while True:
        dseq=diff(dseq)
        count+=1
        if all(dseq==dseq[0]):
            break    
    return count


# In[6]:


power=get_power(seq)
power


# In[7]:


n=arange(1,len(seq)+1)
p=polyfit(n,seq,power)


# In[8]:


int(polyval(p,max(n)+1))


# In[9]:


S="""
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""".strip()
lines=S.split('\n')
seqs=[]
for line in lines:
    seq=array([int(_) for _ in line.split()])
    seqs.append(seq)
seqs


# In[10]:


def predict_next_val(seq):
    power=get_power(seq)
    n=arange(1,len(seq)+1)
    p=polyfit(n,seq,power) 
    val=int(round(polyval(p,max(n)+1)))
    return val    


# In[11]:


for seq in seqs:
    val=predict_next_val(seq)
    print(seq,":",val)


# In[12]:


vals=[predict_next_val(seq) for seq in seqs]
print(sum(vals))


# In[13]:


S=open('data/day9.txt').read()
lines=S.split('\n')
print(len(lines))
seqs=[]
for line in lines:
    if not line:
        continue
    
    seq=array([int(_) for _ in line.split()])
    seqs.append(seq)


# In[14]:


vals=[predict_next_val(seq) for seq in seqs]
print(sum(vals))
    


# In[ ]:




