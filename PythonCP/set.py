#Set is fastest tool in membership testing , deduplication and hash-based operation set is used , internal hash table implement hash table


s = set() 
s = {1,2,3,4}
s = set([1,2,3])
s = set("abd")

s = {} # this is dict not set for set you have to use set() : s = set()

s.add(5)
s.remove(x) #but can give error if x is not present
s.discard(x)
s.pop()


#Membership check
if x in s: 
    ...
    
seen = set()

for x in arr:
    if x in seen:
        print("duplicate")
    
    s.add(s)
    
#Trick for cp 
#Remove Duplicate

arr=[1,1,1,2,3,4,2,1,3]

unique = list(set(arr))

#Fast Look up 
for x in arr:
    if x == target:
        pass
    
lookup = set(arr)

if target in lookup:
    pass

#Two sum classic 
seen = set()

for x in arr:
    if target-x in seen: 
        print("pair found")
        
    set.add(x)
    
#Detect duplicate 
if len(arr) != len(set(arr)):
    print("duplicate exists")
    
s = "abcabcbb"

#sliding window unique string
seen = set()
l=0
for r in range(len(s)):
    while s[r] in seen:
        seen.remove(s[l])
        l +=1
        
    seen.add(s[r])
    

#Intersection of Arrays 
a = {1,2,3}
b = {2,3,4}

c = a & b

# a & b  → intersection
# a | b  → union
# a - b  → difference
# a ^ b  → symmetric difference

# fast diffrence 
remaining = set(a) - set(b)

if x in list :  # slower
    pass 

s = set(list)
if x in s:
    pass

#Use set for graph visited
visited = set()

def dfs(node):
    if node in visited:
        return 
    visited.add(node)
    
#Unique Pair Tracking
pairs = set()

pairs.add((u,v))
#Tuple are hashables, and good for set

#Pattern : Distinct Element in Windows 

from collections import defaultdict

count = defaultdict(int)
distinct = 0

#Check Permutation (a and b are anagram or permutation of each other )
set(a) == set(b)


#Unique Coordinate 
points = set()

points.add((x,y))

# Memory Performance
# Set uses more memory than list because of hash table.
# list  → 8 bytes per element
# set   → ~60+ bytes per element

#Immutable set is frozenset([1,2,3])
visited.add(frozenset(state))