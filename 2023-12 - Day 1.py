#!/usr/bin/env python
# coding: utf-8

# ## Part 1
# 
# 

#     The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
#     
#     For example:
#     
#     1abc2
#     pqr3stu8vwx
#     a1b2c3d4e5f
#     treb7uchet
#     In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.
#     
# 

# In[7]:


from numpy import *


# In[8]:


S="""
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".strip()


# In[9]:


lines=S.split('\n')


# In[10]:


for line in lines:
    pass


# In[11]:


line


# In[15]:


arr=array([ord(_) for _ in line])
arr


# In[16]:


arr=arr[ (arr>=ord('0')) & (arr<=ord('9'))]
arr


# In[19]:


int(chr(arr[0])+chr(arr[-1]))


# In[20]:


nums=[]
for line in lines:
    arr=array([ord(_) for _ in line])
    arr=arr[ (arr>=ord('0')) & (arr<=ord('9'))]
    val=int(chr(arr[0])+chr(arr[-1]))
    nums.append(val)

nums,sum(nums)


# In[21]:


S=open('data/day1.txt').read().strip()
lines=S.split('\n')
len(lines)


# In[22]:


nums=[]
for line in lines:
    arr=array([ord(_) for _ in line])
    arr=arr[ (arr>=ord('0')) & (arr<=ord('9'))]
    val=int(chr(arr[0])+chr(arr[-1]))
    nums.append(val)

sum(nums)


# ## Part 2

#     Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".
#     
#     Equipped with this new information, you now need to find the real first and last digit on each line. For example:
#     
#     two1nine
#     eightwothree
#     abcone2threexyz
#     xtwone3four
#     4nineeightseven2
#     zoneight234
#     7pqrstsixteen
#     In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

# In[32]:


S="""
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".strip()
lines=S.split('\n')
len(lines)


# In[33]:


lines


# In[37]:


nums=[]
for line in lines:
    print(line,"::",end="")

    while True:
        idx=[]
        digit_name=[]   # xtwone3four have to deal with two happening before one
        digits=['zero','one','two','three','four','five','six','seven','eight','nine']
        for i,name in enumerate(digits):
            try:
                idx.append(line.index(name))
                digit_name.append(name)
            except ValueError:
                pass
        if idx:
            i=argmin(idx)
            line=line.replace(digit_name[i],str(digits.index(digit_name[i])))
        else:
            break
                          
    print(line)
        
    
    arr=array([ord(_) for _ in line])
    arr=arr[ (arr>=ord('0')) & (arr<=ord('9'))]
    val=int(chr(arr[0])+chr(arr[-1]))
    nums.append(val)

nums,sum(nums)


# In[28]:





# In[42]:


S=open('data/day1.txt').read().strip()
lines=S.split('\n')
len(lines)


# In[43]:


nums=[]
for line in lines:
    #print(line,"::",end="")
    while True:
        idx=[]
        digit_name=[]   # xtwone3four have to deal with two happening before one
        digits=['zero','one','two','three','four','five','six','seven','eight','nine']
        for i,name in enumerate(digits):
            try:
                idx.append(line.index(name))
                digit_name.append(name)
            except ValueError:
                pass
        if idx:
            i=argmin(idx)
            line=line.replace(digit_name[i],str(digits.index(digit_name[i])))
        else:
            break
                          
        
    #print(line," ",end="")
    arr=array([ord(_) for _ in line])
    arr=arr[ (arr>=ord('0')) & (arr<=ord('9'))]
    val=int(chr(arr[0])+chr(arr[-1]))
    #print(val)
    nums.append(val)

sum(nums)


# In[47]:


min(nums),max(nums)


# somehow this is wrong?  compare to someone elses solution to see which line I'm failing.  it's zfxbzhczcx9eightwockk

# In[81]:


import re

file = open('data/day1.txt', 'r')
lines = [line.rstrip() for line in file]
digits = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
totParte1 = 0 
totParte2 = 0 

def parte1(lines):
	somma = 0
	for line in lines:
		num = [c for c in line if c.isnumeric()]
		somma += int(num[0]+num[-1])
	return somma

def parte2(lines):
    somma = 0
    vals=[]
    r = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'
    pattern = re.compile(r)
    for line in lines:
        words = []
        for word in pattern.findall(line):
            if(word in digits):
                words.append(str(digits[word]))
            else: 
                words.append(word)	
                
        vals.append(int(words[0]+words[-1]))
        somma += int(words[0]+words[-1])
    return somma,vals

totParte1 = parte1(lines)
totParte2,vals = parte2(lines)
print(totParte2)


# In[82]:


len(vals),len(nums)


# In[83]:


idx=where(array(vals)!=array(nums))[0]


# In[84]:


idx


# In[85]:


lines[14]


# In[86]:


vals[14]


# In[87]:


nums[14]


# In[88]:


nums=[]
for line in lines:
    #print(line,"::",end="")
    while True:
        idx=[]
        digit_name=[]   # xtwone3four have to deal with two happening before one and zfxbzhczcx9eightwockk  yuck!  have to iterate chars
        digits=['zero','one','two','three','four','five','six','seven','eight','nine']
        for i,name in enumerate(digits):
            try:
                idx.append(line.index(name))
                digit_name.append(name)
            except ValueError:
                pass
        if idx:
            i=argmin(idx)
            line=line.replace(digit_name[i],str(digits.index(digit_name[i])))
        else:
            break
                          
        
    #print(line," ",end="")
    arr=array([ord(_) for _ in line])
    arr=arr[ (arr>=ord('0')) & (arr<=ord('9'))]
    val=int(chr(arr[0])+chr(arr[-1]))
    #print(val)
    nums.append(val)

sum(nums)


# In[68]:


line


# In[76]:


def find_first(line):

    D={'zero':0,
       'one':1,
       'two':2,
       'three':3,
       'four':4,
       'five':5,
       'six':6,
       'seven':7,
       'eight':8,
       'nine':9}

    for i in range(10):
        D[str(i)]=i
    idx=[]
    all_keys=[]
    for key in D:
        try:
            idx.append(line.index(key))
            all_keys.append(key)
        except ValueError:
            pass
         
    i=argmin(idx)
    digit=str(D[all_keys[i]])

    return digit


def find_last(line):

    D={'zero':0,
       'one':1,
       'two':2,
       'three':3,
       'four':4,
       'five':5,
       'six':6,
       'seven':7,
       'eight':8,
       'nine':9}

    line=line[::-1]  # reverse
    for i in range(10):
        D[str(i)]=i
    idx=[]
    all_keys=[]
    for key in D:
        try:
            idx.append(line.index(key[::-1]))
            all_keys.append(key)
        except ValueError:
            pass
         
    i=argmin(idx)
    digit=str(D[all_keys[i]])

    return digit


# In[77]:


line


# In[79]:


find_first(line),find_last(line)


# In[80]:


for line in lines[:20]:
    print(line,"::",end="")
    print(find_first(line),find_last(line))


# In[89]:


nums=[]
for line in lines:
    val=int(find_first(line)+find_last(line))
    nums.append(val)

sum(nums)


# In[ ]:




