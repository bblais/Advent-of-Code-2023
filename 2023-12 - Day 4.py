#!/usr/bin/env python
# coding: utf-8

#     For example:
#     
#     Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
#     Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
#     Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
#     Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
#     Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
#     Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
#     In the above example, card 1 has five winning numbers (41, 48, 83, 86, and 17) and eight numbers you have (83, 86, 6, 31, 17, 9, 48, and 53). Of the numbers you have, four of them (48, 83, 17, and 86) are winning numbers! That means card 1 is worth 8 points (1 for the first match, then doubled three times for each of the three matches after the first).
#     
#     Card 2 has two winning numbers (32 and 61), so it is worth 2 points.
#     Card 3 has two winning numbers (1 and 21), so it is worth 2 points.
#     Card 4 has one winning number (84), so it is worth 1 point.
#     Card 5 has no winning numbers, so it is worth no points.
#     Card 6 has no winning numbers, so it is worth no points.
#     So, in this example, the Elf's pile of scratchcards is worth 13 points.
#     
# 

# In[1]:


S="""
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
""".strip()


# In[2]:


lines=S.split('\n')
line=lines[0]


# In[3]:


line


# In[4]:


data=[]
for line in lines:
    data.append(
    [[int(_) for _ in line.split(':')[1].split('|')[0].split()],
        [int(_) for _ in line.split(':')[1].split('|')[1].split()]]
    )
data


# In[5]:


total=0
for part1,part2 in data:
    overlap=list(set(part1)&set(part2))
    if overlap:
        total+=2**(len(overlap)-1)
    print(overlap)

print(total)


# In[6]:


S=open('data/day4.txt').read().strip()
lines=S.split('\n')
len(lines)


# In[7]:


data=[]
for line in lines:
    data.append(
    [[int(_) for _ in line.split(':')[1].split('|')[0].split()],
        [int(_) for _ in line.split(':')[1].split('|')[1].split()]]
    )

total=0
for part1,part2 in data:
    overlap=list(set(part1)&set(part2))
    if overlap:
        total+=2**(len(overlap)-1)

print(total)


#     This time, the above example goes differently:
#     
#     Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
#     Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
#     Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
#     Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
#     Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
#     Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
#     Card 1 has four matching numbers, so you win one copy each of the next four cards: cards 2, 3, 4, and 5.
#     Your original card 2 has two matching numbers, so you win one copy each of cards 3 and 4.
#     Your copy of card 2 also wins one copy each of cards 3 and 4.
#     Your four instances of card 3 (one original and three copies) have two matching numbers, so you win four copies each of cards 4 and 5.
#     Your eight instances of card 4 (one original and seven copies) have one matching number, so you win eight copies of card 5.
#     Your fourteen instances of card 5 (one original and thirteen copies) have no matching numbers and win no more cards.
#     Your one instance of card 6 (one original) has no matching numbers and wins no more cards.
#     Once all of the originals and copies have been processed, you end up with 1 instance of card 1, 2 instances of card 2, 4 instances of card 3, 8 instances of card 4, 14 instances of card 5, and 1 instance of card 6. In total, this example pile of scratchcards causes you to ultimately have 30 scratchcards!

# In[8]:


S="""
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
""".strip()


# In[9]:


lines=S.split('\n')
line=lines[0]


# In[10]:


data=[]
for line in lines:
    data.append(
    [[int(_) for _ in line.split(':')[1].split('|')[0].split()],
        [int(_) for _ in line.split(':')[1].split('|')[1].split()]]
    )
data


# In[15]:


total=0
copies=[1]*len(data)
for i,(part1,part2) in enumerate(data):
    overlap=list(set(part1)&set(part2))
    if overlap:
        L=len(overlap)
        print("Copying...",end="")
        for j in range(i+1,i+L+1):
            print(j," ",end="")
            copies[j]+=copies[i]
        print()
    print(copies[i],overlap)

print(copies)
print(sum(copies))


# In[16]:


S=open('data/day4.txt').read().strip()
lines=S.split('\n')
len(lines)


# In[18]:


data=[]
for line in lines:
    data.append(
    [[int(_) for _ in line.split(':')[1].split('|')[0].split()],
        [int(_) for _ in line.split(':')[1].split('|')[1].split()]]
    )


# In[19]:


total=0
copies=[1]*len(data)
for i,(part1,part2) in enumerate(data):
    overlap=list(set(part1)&set(part2))
    if overlap:
        L=len(overlap)
        #print("Copying...",end="")
        for j in range(i+1,i+L+1):
            #print(j," ",end="")
            copies[j]+=copies[i]
        #print()
    #print(copies[i],overlap)

#print(copies)
print(sum(copies))


# In[ ]:




