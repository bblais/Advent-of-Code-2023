#!/usr/bin/env python
# coding: utf-8

# ## Example
#     
#     467..114..
#     ...*......
#     ..35..633.
#     ......#...
#     617*......
#     .....+.58.
#     ..592.....
#     ......755.
#     ...$.*....
#     .664.598..
#     In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

# In[1]:


S="""
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".strip()


# In[3]:


print(S)


# In[8]:


lines=S.split('\n')
line=lines[0]
R=len(lines)
C=len(line)


# In[9]:


line


# In[16]:


def neighbors(r,c):

    if c>0:
        yield r,c-1

        if r>0:
            yield r-1,c-1

        if r<R-1:
            yield r+1,c-1
    if c<C-1:
        yield r,c+1

        if r>0:
            yield r-1,c+1

        if r<R-1:
            yield r+1,c+1

    if r>0:
        yield r-1,c

    if r<R-1:
        yield r+1,c
    


# In[13]:


data=[]
for row in range(R):
    locs=[]
    ss=''
    for col in range(C):
        character=lines[row][col]
        if character in '0123456789':
            ss+=character
            locs.append((row,col))
        elif ss:
            val=int(ss)
            data.append([val,locs])
            locs=[]
            ss=''
    if ss:
        val=int(ss)
        data.append([val,locs])

data
            


# In[15]:


print(S)


# In[17]:


result=[]
for val, locs in data:
    found=False
    for r,c in locs:
        for rn,cn in neighbors(r,c):
            if lines[rn][cn] not in '0123456789.':
                found=True
                result.append(val)
                break
        if found:
            break
print(result)


# In[18]:


sum(result)


# ## Part 1

# In[19]:


S=open('data/day3.txt').read().strip()
lines=S.split('\n')
len(lines)


# In[20]:


lines=S.split('\n')
line=lines[0]
R=len(lines)
C=len(line)


# In[21]:


data=[]
for row in range(R):
    locs=[]
    ss=''
    for col in range(C):
        character=lines[row][col]
        if character in '0123456789':
            ss+=character
            locs.append((row,col))
        elif ss:
            val=int(ss)
            data.append([val,locs])
            locs=[]
            ss=''
    if ss:
        val=int(ss)
        data.append([val,locs])


            


# In[23]:


result=[]
for val, locs in data:
    found=False
    for r,c in locs:
        for rn,cn in neighbors(r,c):
            if lines[rn][cn] not in '0123456789.':
                found=True
                result.append(val)
                break
        if found:
            break
print(sum(result))


# ## Part 2
# 
#     Consider the same engine schematic again:
#     
#     467..114..
#     ...*......
#     ..35..633.
#     ......#...
#     617*......
#     .....+.58.
#     ..592.....
#     ......755.
#     ...$.*....
#     .664.598..
#     In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

# In[24]:


S="""
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".strip()


# In[25]:


lines=S.split('\n')
line=lines[0]
R=len(lines)
C=len(line)


# In[26]:


data=[]
for row in range(R):
    locs=[]
    ss=''
    for col in range(C):
        character=lines[row][col]
        if character in '0123456789':
            ss+=character
            locs.append((row,col))
        elif ss:
            val=int(ss)
            data.append([val,locs])
            locs=[]
            ss=''
    if ss:
        val=int(ss)
        data.append([val,locs])


            


# In[33]:


from numpy import prod


# In[34]:


total=0
for row in range(R):
    for col in range(C):
        character=lines[row][col]
        if not character=='*':
            continue

        vals=[]
        for val, locs in data:
            for rn,cn in neighbors(row,col):
                if (rn,cn) in locs:
                    vals.append(val)
                    break
        if len(vals)==2:
            print(vals)
            total+=prod(vals)


print(total)
            
                    


# In[35]:


S=open('data/day3.txt').read().strip()
lines=S.split('\n')
len(lines)


# In[36]:


lines=S.split('\n')
line=lines[0]
R=len(lines)
C=len(line)


# In[37]:


data=[]
for row in range(R):
    locs=[]
    ss=''
    for col in range(C):
        character=lines[row][col]
        if character in '0123456789':
            ss+=character
            locs.append((row,col))
        elif ss:
            val=int(ss)
            data.append([val,locs])
            locs=[]
            ss=''
    if ss:
        val=int(ss)
        data.append([val,locs])


            


# In[38]:


total=0
for row in range(R):
    for col in range(C):
        character=lines[row][col]
        if not character=='*':
            continue

        vals=[]
        for val, locs in data:
            for rn,cn in neighbors(row,col):
                if (rn,cn) in locs:
                    vals.append(val)
                    break
        if len(vals)==2:
            print(vals)
            total+=prod(vals)


print(total)
            
                    


# In[ ]:




