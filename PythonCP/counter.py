#Counter is the high performance frequency table 

from collections import Counter

arr=[1,2,2,3,3,3]

cnt = Counter(arr)

print(cnt)
# Counter({3:3, 2:2, 1:1})
# Problem type:
# duplicates
# majority element
# frequency based sorting
#O(n)
cnt = Counter(arr)

for num,freq in cnt.items():
    if freq >1:
        print(num)
        
#Get Top K Frequent 
cnt = Counter(arr)
# Used in problems like:
# top k frequent elements
# most frequent words
# O(n log k)
top_k = cnt.most_common(3)
print(top_k)

#Fast String Frequency 
from collections import Counter

s="aabbac"

cnt = Counter(s)

print(cnt)
# Check Anagram in O(n)
Counter(s1)==Counter(s2)
Counter("silent")==Counter("listen")

#Remove element from counter subtraction 
cnt = Counter([1,1,1,2,2,3])

cnt.subtract([1,2])

print(cnt) #Counter({1:2,2:1,3:1})

# Multiset Intersection
# min(freq)
a = Counter([1,1,2,3])
b = Counter([1,2,2,3])

print(a & b)

Counter({1:1,2:1,3:1})

# Multiset Union
print(a | b)
# max(freq)

# Convert Counter-> List
cnt = Counter([1,1,2])
list(cnt.elements())

#CP tricks 
d[x] = d.get(x,0) + 1
cnt[x] +=1


cnt = Counter()

for x in arr: 
    cnt[x]+=1
    d[x] = d.get(x,0) + 1
    
#Sliding window 
need = Counter(t)
window = Counter()

have = 0
need_count  = len(need)

cnt = Counter(s)

for char, freq in cnt.most_comman():
    print(char,freq)
    
#Counter + Greedy Pattern
cnt = Counter(s)

for char, freq in cnt.most_common():
    print(char, freq)
    
#Counter + Heap Pattern 
import heapq

cnt = Counter(arr)

heap=[(-v,k) for k,v in cnt.items()]
heapq.heapify(heap)

#Counter Arthimetic 
a = Counter("aaaabbbbccc")
b = Counter("bacbac")

print(a+b) #Additon -> {a:6,b:6,c:5}
print(a-b) #subtract -> {a:2,b:2,c:1}
print(a&b) #Intersection:min(freq)->{a:2,b:2,c:2}
print(a|b) #Union:max(freq)->{a:4,b:4,c:3}