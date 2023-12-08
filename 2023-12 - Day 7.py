#!/usr/bin/env python
# coding: utf-8

# https://adventofcode.com/2023/day/7

# In[66]:


S="""
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""
lines=S.strip().split("\n")
hands,bids=zip(*[_.split() for _ in lines])
bids=[int(_) for _ in bids]
hands,bids


# In[67]:


card_vals={}
for i,card in enumerate('23456789TJQKA'):
    card_vals[card]=i+2
card_vals


# In[68]:


hand='QQQ3Q'
s=set(hand)


# In[69]:


s


# In[70]:


sorted([hand.count(_) for _ in s],reverse=True)


# In[71]:


len(s)


# In[72]:


hand_ranks={'five of a kind':7,
            'four of a kind':6,
            'full house':5,
            'three of a kind':4,
            'two pair':3,
            'one pair':2,
            'high card':1}


# In[137]:


def get_type(hand):
    assert len(hand)==5
    
    s=set(hand)
    if len(s)==1:
        return 'five of a kind'

    counts=sorted([hand.count(_) for _ in s],reverse=True)

    if counts[0]==4:
        return 'four of a kind'

    if counts[0]==3 and counts[1]==2:
        return 'full house'

    if counts[0]==3:
        return 'three of a kind'

    if counts[0]==2 and counts[1]==2:
        return 'two pair'

    if counts[0]==2:
        return 'one pair'

    return 'high card'


# In[138]:


def value(hand):
    val=hand_ranks[get_type(hand)]

    for i,c in enumerate(hand):
        val+=card_vals[c]/14**(i+2)

    return val


# In[75]:


from numpy import arange


# In[76]:


arange(2,14)/14/100


# In[77]:


vals2,bids2=zip(*sorted(zip([value(_) for _ in hands],bids)))
bids2


# In[78]:


(bids2*arange(1,len(bids2)+1)).sum()


# In[79]:


S=open('data/day7.txt').read().strip()
lines=S.split('\n')
len(lines)


# In[80]:


lines=S.strip().split("\n")
hands,bids=zip(*[_.split() for _ in lines])
bids=[int(_) for _ in bids]


# In[81]:


vals2,bids2=zip(*sorted(zip([value(_) for _ in hands],bids)))
(bids2*arange(1,len(bids2)+1)).sum()


# ## Part 2

# In[97]:


card_vals={}
for i,card in enumerate('J23456789TQKA'):
    card_vals[card]=i+2
card_vals


# In[157]:


def get_typeJ(hand):
    assert len(hand)==5

    s=set(hand)

    
    if len(s)==1:
        return 'five of a kind'  # unchanged

    J=hand.count('J')
    hand2=hand.replace('J','')
    
    s=set(hand2)
    
    counts=sorted([hand.count(_) for _ in s],reverse=True)

    try:
        counts[0]+=J
    except IndexError:
        print(hand)
        raise

    assert sum(counts)==5

    if counts[0]==5:
        return 'five of a kind'
    
    if counts[0]==4:
        return 'four of a kind'

    if counts[0]==3 and counts[1]==2:
        return 'full house'

    if counts[0]==3:
        return 'three of a kind'

    if counts[0]==2 and counts[1]==2:
        return 'two pair'

    if counts[0]==2:
        return 'one pair'

    return 'high card'

def valueJ(hand):

    card_valsJ={}
    for i,card in enumerate('J23456789TQKA'):
        card_valsJ[card]=i+2
    
    val=hand_ranks[get_typeJ(hand)]

    for i,c in enumerate(hand):
        val+=card_valsJ[c]/14**(i+2)

    return val


# In[158]:


S="""
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""
lines=S.strip().split("\n")
hands,bids=zip(*[_.split() for _ in lines])
bids=[int(_) for _ in bids]
hands,bids


# In[159]:


vals2,bids2=zip(*sorted(zip([valueJ(_) for _ in hands],bids)))
(bids2*arange(1,len(bids2)+1)).sum()


# In[160]:


S=open('data/day7.txt').read().strip()
lines=S.split('\n')
len(lines)


# In[161]:


lines=S.strip().split("\n")
hands,bids=zip(*[_.split() for _ in lines])
bids=[int(_) for _ in bids]


# In[162]:


vals2,bids2=zip(*sorted(zip([valueJ(_) for _ in hands],bids)))
(bids2*arange(1,len(bids2)+1)).sum()


# In[163]:


Jhands=[_ for _ in hands if 'J' in _]
len(Jhands)


# In[156]:


Jhands[:10]


# In[148]:


for hand in Jhands:
    print(hand,"=",get_typeJ(hand))


# In[ ]:




