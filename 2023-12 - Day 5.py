#!/usr/bin/env python
# coding: utf-8

#     The almanac (your puzzle input) lists all of the seeds that need to be planted. It also lists what type of soil to use with each kind of seed, what type of fertilizer to use with each kind of soil, what type of water to use with each kind of fertilizer, and so on. Every type of seed, soil, fertilizer and so on is identified with a number, but numbers are reused by each category - that is, soil 123 and fertilizer 123 aren't necessarily related to each other.
#     
#     For example:
#     
#     seeds: 79 14 55 13
#     
#     seed-to-soil map:
#     50 98 2
#     52 50 48
#     
#     soil-to-fertilizer map:
#     0 15 37
#     37 52 2
#     39 0 15
#     
#     fertilizer-to-water map:
#     49 53 8
#     0 11 42
#     42 0 7
#     57 7 4
#     
#     water-to-light map:
#     88 18 7
#     18 25 70
#     
#     light-to-temperature map:
#     45 77 23
#     81 45 19
#     68 64 13
#     
#     temperature-to-humidity map:
#     0 69 1
#     1 0 69
#     
#     humidity-to-location map:
#     60 56 37
#     56 93 4
#     The almanac starts by listing which seeds need to be planted: seeds 79, 14, 55, and 13.
#     
#     The rest of the almanac contains a list of maps which describe how to convert numbers from a source category into numbers in a destination category. That is, the section that starts with seed-to-soil map: describes how to convert a seed number (the source) to a soil number (the destination). This lets the gardener and his team know which soil to use with which seeds, which water to use with which fertilizer, and so on.
#     
#     Rather than list every source number and its corresponding destination number one by one, the maps describe entire ranges of numbers that can be converted. Each line within a map contains three numbers: the destination range start, the source range start, and the range length.
#     
#     Consider again the example seed-to-soil map:
#     
#     50 98 2
#     52 50 48
#     The first line has a destination range start of 50, a source range start of 98, and a range length of 2. This line means that the source range starts at 98 and contains two values: 98 and 99. The destination range is the same length, but it starts at 50, so its two values are 50 and 51. With this information, you know that seed number 98 corresponds to soil number 50 and that seed number 99 corresponds to soil number 51.
#     
#     The second line means that the source range starts at 50 and contains 48 values: 50, 51, ..., 96, 97. This corresponds to a destination range starting at 52 and also containing 48 values: 52, 53, ..., 98, 99. So, seed number 53 corresponds to soil number 55.
#     
#     Any source numbers that aren't mapped correspond to the same destination number. So, seed number 10 corresponds to soil number 10.
#     
#     So, the entire list of seed numbers and their corresponding soil numbers looks like this:
#     
#     seed  soil
#     0     0
#     1     1
#     ...   ...
#     48    48
#     49    49
#     50    52
#     51    53
#     ...   ...
#     96    98
#     97    99
#     98    50
#     99    51
#     With this map, you can look up the soil number required for each initial seed number:
#     
#     Seed number 79 corresponds to soil number 81.
#     Seed number 14 corresponds to soil number 14.
#     Seed number 55 corresponds to soil number 57.
#     Seed number 13 corresponds to soil number 13.
#     The gardener and his team want to get started as soon as possible, so they'd like to know the closest location that needs a seed. Using these maps, find the lowest location number that corresponds to any of the initial seeds. To do this, you'll need to convert each seed number through other categories until you can find its corresponding location number. In this example, the corresponding types are:
#     
#     Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
#     Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
#     Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
#     Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.
#     So, the lowest location number in this example is 35.
#     
#     What is the lowest location number that corresponds to any of the initial seed numbers?

# In[2]:


S="""
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""
lines=S.split("\n")


# In[53]:


class Map:

    def __init__(self,line):
        self.source=line.split('-')[0]
        self.destination=line.split('-')[-1].split(' ')[0]
        self.ranges=[]
        
    def __repr__(self):
        S=f"{self.source} to {self.destination}"
        if self.ranges:
            S+=str(self.ranges)
        return S

    def _add_range(self,line):
        vals=[int(_) for _ in line.split()]
        self.ranges.append(vals)



    def __getitem__(self,item):
        src_index=None
        dst_index=None
        for d,s,l in self.ranges:
            if s<=item<=s+l:
                src_index=item
                dst_index=(item-s)+d
                break

        if src_index is None:
            src_index=item
            dst_index=item

        return self.source,src_index,self.destination,dst_index


# In[54]:


maps={}
m=None
for line in lines:
    if line.startswith('seeds:'):
        seeds=[int(_) for _ in line.split(":")[1].split()]
        continue

    if line and line[0] not in '0123456789':
        m=Map(line)
        continue 
        
    if not line and m:
        maps[m.source]=m
        m=None
    elif m:
        m._add_range(line)
        

print(seeds)
print(maps)


# In[55]:


m=maps['seed']
m


# In[56]:


m[300]


# In[57]:


m[99]


# In[58]:


for i in range(100):
    print(m[i])


# In[59]:


name,val='seed',79

while True:
    m=maps[name]
    src,src_i,dst,dst_i=m[val]
    print(src,src_i,dst,dst_i)

    name,val=dst,dst_i

    if name not in maps:
        break


# In[60]:


dst_i


# In[61]:


def get_location(maps,seed=None,verbose=False):
    name,val='seed',seed
    
    while True:
        m=maps[name]
        src,src_i,dst,dst_i=m[val]
        if verbose:
            print(src,src_i,dst,dst_i)
    
        name,val=dst,dst_i
    
        if name not in maps:
            break  

    assert name=='location'
    return dst_i


# In[62]:


get_location(maps,seed=79,verbose=True)


# In[63]:


[get_location(maps,seed=seed) for seed in seeds]


# In[64]:


min([get_location(maps,seed=seed) for seed in seeds])


# In[71]:


S=open('data/day5.txt').read().strip()
lines=S.split('\n')
len(lines)


# In[76]:


maps={}
m=None
for line in lines:
    if line.startswith('seeds:'):
        seeds=[int(_) for _ in line.split(":")[1].split()]
        continue

    if line and line[0] not in '0123456789':
        m=Map(line)
        continue 
        
    if not line and m:
        maps[m.source]=m
        m=None
    elif m:
        m._add_range(line)
        
if m:
    maps[m.source]=m
    


# In[77]:


seeds


# In[78]:


min([get_location(maps,seed=seed) for seed in seeds])


# In[ ]:




