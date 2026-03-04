d = {} 
d = dict()

d = {"a":1 , "b":2}

pairs = [("a",1),("b",2)]
d=dict(pairs)

d={i:i*i for i in range(5)}
#{0:0 ,1:1,2:4,3:9,4:16}

d["apple"] = 3

d["apple"] = 5

d["apple"]

d.get("apple",0) #this is safe look up and this is preferred

del d["apple"]

d.pop("apple",None) #this is safe delete

#Membership test

if key in d: 
    pass

if x in freq:
    print(freq[x])
    
#Iteration 
#On key
for k in d:
    pass
#ON values
for v in d.values():
    pass

#On key and values both:
for k,v in d.items():
    
#Length
len(d)

#Important Methods
d.get(key,default) #safe look up
d.pop(key, None) #safe remove 

count = d.get(x,0)

#setDefault(If key is not present then set this value in the key as default)
d.setdefault(key,default)

d.setdefault("a",0)

#pop()
d.pop(key)
d.pop(key,default)

#popItem() : to remove last inserted item
d.popitem() 

#key()
d.key() 

#values()
d.values()

#items
d.items()

#clear
d.clear()

#updates()
d.update(other_dict)

d1:dict = {'a':1}
d2:dict = {'b':2}

d1.update(d2)
{'a':1, 'b':2}

d2 = d.copy()

#Sorting 
#Sort by keys
sorted(d.items())

#Sort by values
sorted(d.items, key=lambda x:x[1])

#Sort by values in descending order
sorted(d.items, key=lambda x:x[1] , reverse=True )

#Patterns 
#Standard
freq = {}

for x in arr: 
    freq[x]=freq.get(x,0) + 1
    
#Counter
from collections import Counter

freq = Counter(arr)

#defaultdict : 
from collections import defaultdict

d = defaultdict(int)
d['a']+=1

d = defaultdict(list)

d[1].append(2)

d=defaultdict()


#Dictionary as Graph 
from collections import defaultdict

graph = defaultdict(list)

graph[1].append(2)
graph[2].append(3)

#Reverse Mapping Pattern 
# values-> list of keys
from collections import defaultdict

rev = defaultdict(list)

for k,v in d.items():
    rev[v].append(k)
    
#Coordination compression 
arr=[100,500,1000]
comp = {v:i for i,v in enumerate(sorted(set(arr)))}
"100->0,500->1,1000->2"

#Prefix Sum + hashmap Pattern 

"count subarray with sum == k"
prefix =0
count =0
d={0:1}

for x in arr: 
    prefix+=x
    count += d.get(prefix-k,0)
    d[prefix] = d.get(prefix,0)+1
    
    
"two sum pattern"

nums = [2,7,11,15]

target= 9 

seen = {} 

for i,v in enumerate(nums):
    if target - v in seen:
        print(seen[target-v],i)
    
    seen[v]=i
    
"Memorization Pattern"
memo = {}

def solve(x):
    if x in memo:
        return memo[x]
    
    ans = x + solve(x-1)
    
    memo[x] = ans
    return ans

"Grouping Pattern"
"Group anagram"
from collections import defaultdict

groups = defaultdict(list)

for word in words:
    key = tuple(sorted(word))
    groups[key].append(word)

"Sliding window + dict"
"longest substring without repeating"
last = {}
l = 0
ans = 0

for r,c in enumerate(s):
    if c in last: 
        l = max(l, last[c]+1)
        
    last[c]=r
    ans = max(ans,r-l+1)


#Performance tricks 
#Local Bindig
get = d.get

for x in arr: 
    d[x]=get(x,0)+1
    
#Prefer list when key are small
freq = {} # Bad 
freq = [0]*(10**6) #Better

#Default dict is subclass of dict in collection and it is better than dict in three ways :
#Missing Key Errors are solved because default values are already set , no need to write boiler plate code to like this ```code : if key not in d: d[key]=0 ```
d[key] = d.get(key,0)+1

#Cleaner code ```code: if key not in graph; graph[key]=[] graph[key].append[values]```
graph[key].append(values)

#Faster in loops : when we need to append lot of values to dict default dict is faster 
# defaultdict + append 

# Patterns
from collections import defaultdict

freq=defaultdict(int)

for x in arr:
    freq[x]+=1
    
graph = defaultdict(list)

graph[1].append(2)
graph[2].append(3)

groups = defaultdict(set)

groups["a"].add(1)
groups["a"].add(1) #{a:{1}}

d = defaultdict(dict)
d["user1"]["score"] = 100
{
    'user1':{'score':100}
}

#Patterns for CP 
#Frequency
freq = defaultdict(int)

for x in arr:
    freq[x]+=1

#Graph Adjacency List    
graph=defaultdict(list)

for u,v in edges:
    graph[u].append(v)
    
#Reverse Index:values->position

pos = defaultdict(list)
    
for i, v in enumerate(arr):
    pos[v].append(i)
    
#Grouping(group words by length)
groups = defaultdict(list)

for w in words:
    groups[len(w)].append(w)
    
#Unique Grouping

groups = defaultdict(set)

for a,b in pairs:
    groups[a].add(b)
    
#Prefix Sum + hashmap
prefix = 0
d =defaultdict(int)

d[0]=1

for x in arr:
    prefix +=x
    count += d[prefix-k]
    d[prefix] +=1
    
#Graph BFS
graph = defaultdict(list)

for u,v in edges:
   graph[u].append(v)
   
#Counting Pairs
count = defaultdict(int)
# Pair with same remainder
for x in arr:
    r=x%k
    ans+=count[r]
    count[r]+=1
    
