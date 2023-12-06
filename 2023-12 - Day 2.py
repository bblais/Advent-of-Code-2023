#!/usr/bin/env python
# coding: utf-8

# https://adventofcode.com/2023/day/2
#     
#     For example, the record of a few games might look like this:
#     
#     Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
#     Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
#     Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
#     Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
#     Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
#     In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.
#     
#     The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
#     
#     In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.

# In[3]:


S="""
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""".strip()
lines=S.split('\n')


# In[22]:


global verbose
verbose=False


# In[23]:


import builtins

def print(*args, **kwargs):
    global verbose
    if verbose:
        return builtins.print(*args, **kwargs)


# In[24]:


print("hello")


# In[26]:


limits={'red':12,'green':13,'blue':14}


total=0
for line in lines:
    print(line)
    game_id=int(line.split(':')[0].split(' ')[-1])
    sets=line.split(':')[-1].split(';')

    stop=False
    for cube_set in sets:
        parts=cube_set.split(',')
        for part in parts:
            val,color=int(part.split()[0]),part.split()[1]
            limit=limits.get(color,1e500)
            print("\t",val,color,limit,end="")
            if val>limit:
                print(" BAD")
                stop=True
                break
            else:
                print(" OK")
        if stop:
            break
    if not stop:        
        total+=game_id


total


# In[27]:


S=open('data/day2.txt').read().strip()
lines=S.split('\n')
len(lines)


# In[29]:


limits={'red':12,'green':13,'blue':14}

total=0
for line in lines:
    print(line)
    game_id=int(line.split(':')[0].split(' ')[-1])
    sets=line.split(':')[-1].split(';')

    stop=False
    for cube_set in sets:
        parts=cube_set.split(',')
        for part in parts:
            val,color=int(part.split()[0]),part.split()[1]
            limit=limits.get(color,1e500)
            print("\t",val,color,limit,end="")
            if val>limit:
                print(" BAD")
                stop=True
                break
            else:
                print(" OK")
        if stop:
            break
    if not stop:        
        total+=game_id


total


# ## Part 2
# 
#     what is the fewest number of cubes of each color that could have been in the bag to make the game possible?
#     
#     Again consider the example games from earlier:
#     
#     Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
#     Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
#     Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
#     Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
#     Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
#     In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
#     Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
#     Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
#     Game 4 required at least 14 red, 3 green, and 15 blue cubes.
#     Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.
#     The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.
#     
#     For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?

# In[30]:





# In[31]:


S="""
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""".strip()
lines=S.split('\n')


# In[32]:


verbose=True
total=0
for line in lines:
    print(line)
    game_id=int(line.split(':')[0].split(' ')[-1])
    sets=line.split(':')[-1].split(';')

    stop=False
    limits={'red':[],'green':[],'blue':[]}
    for cube_set in sets:
        parts=cube_set.split(',')
        for part in parts:
            val,color=int(part.split()[0]),part.split()[1]
            print("\t",val,color)

            limits[color].append(val)

    power=1
    for key in limits:
        power*=max(limits[key])
    print("\t","power:",power)
    total+=power

total


# In[33]:


S=open('data/day2.txt').read().strip()
lines=S.split('\n')
len(lines)


# In[34]:


verbose=False
total=0
for line in lines:
    print(line)
    game_id=int(line.split(':')[0].split(' ')[-1])
    sets=line.split(':')[-1].split(';')

    stop=False
    limits={'red':[],'green':[],'blue':[]}
    for cube_set in sets:
        parts=cube_set.split(',')
        for part in parts:
            val,color=int(part.split()[0]),part.split()[1]
            print("\t",val,color)

            limits[color].append(val)

    power=1
    for key in limits:
        power*=max(limits[key])
    print("\t","power:",power)
    total+=power

total


# In[ ]:




