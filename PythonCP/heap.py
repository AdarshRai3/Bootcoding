import heapq
#Allow inserting and removal in O(log N)
#Allow searching in O(n)

h=[]

#push
heapq.heappush(h,x)

#pop smallest number
x = heapq.heapqpop(h)

#peek the smallest element
x=h[0] 

#push + pop (faster than separate ops)
heapq.heappushpop(h,x)

#pop then push
heapq.heapreplace(h,x)

#convert list -> heap
heapq.heapify(arr)

#Complexity : 
# push : O(log n)
# pop  : O(log n)
# peek : O(1)
# heapify : O(n)

#Python doesn't have max heap but what we can do we can invert the min heap to produce the max heap
heapq.heappush(h,-x)

x = -heapq.heappop(h)

#Heap with Pairs and heap sort by first tuple element 
heapq.heappush(h,(priority, value))

h=[]

heapq.heappush(h,(2, "taskB"))
heapq.heappush(h,(1,"taskA"))

heapq.heappop(h)

# Top k pattern 
# Pattern : Maintain Heap of size K

import heapq

nums = [9,4,7,1,3,6]

k = 3

h= []

for x in nums : 
    heapq.heappush(h,x)
    
    if len(x) > h:
        heapq.heappop(h)
        
print(h)

# Time Complexity : O(n (log k))

# K Smallest /Largest 
heapq.nsmallest(k,arr)
heapq.nlargest(k,arr)

# Mannual heap is faster in context when streaming
# max heap -> left side
# min heap -> right side


#Streaming median or whenever you find you have to code for input which is streaming, one things you must look at is streaming
import heapq

low =[] #min heap
high =[] #max heap

def add(x):
    
    heapq.heappush(low, -x)
    heapq.heappush(high, -heapq.heapop(low))
    
    if len(high)>len(low):
        heapq.heappush(low, -heapq.heappop(high))

def median():
    return -low[0]

#Heap of Dijastra(shortest path algorithm for non-negative weighted graph )

import heapq

dist = [float('inf')] * n
dist[src] = 0

pq = [(0,src)]

while pq:
    d,node = heapq.heappop(pq)
    
    if d > dist[node]:
        continue 
    
    for nei , w in graph[node]:
        
        nd =d + w
        
        if nd < dist[node]: 
            dist[nei]=nd
            heapq.heappush(pq,(nd,nei))
        
        

#Heap for Greedy Scheduling
#Minimum Meeting Rooms : sort + heap
intervals.sort()

h=[]

for s, e in intervals:
    
    if h and h[0] <=s:
        heapq.heappop(h)
        
    heapq.heappush(h,e)

print(len(h))

#Lazy Deletion Pattern 

# Python heap cannot delete arbitrary element effeciently 
# therefore we have to use lazy deletion pattern

# Concept: Push element normally but when popping ignore invalid entries

# Instead of deleting the element from the heap we just use a hash map and mark that element as invalid , when poping we discard the element.
# This optimisation is helpful beacuse this way we avoiding rebuilding the heap , this keep time complexity O(log n)
# instead of O(n) removal from heap

#Basic Lazy Deletion: 
import heapq
from collections import Counter

heap=[]
deleted=Counter()

def push(x):
    heapq.heappush(heap,x)
    
def remove(x):
    deleted[x]+=1
    
def clean():
    while heap and deleted[heap[0]]:
        deleted[heap[0]]-=1
        heapq.heappop(heap)

def pop():
    clean()
    return heapq.heappop(heap)

def top():
    clean()
    return heap[0]


#2 Lazy Deletion for Max Heap
heapq.heappush(heap,-x)

deleted[-x]

#Sliding Window Median(Classic Lazy Deletion Problem)
#max heap -> left side
#min heap -> right side 
#delayed dict -> lazy deletion

#Code:
import heapq
from collections import Counter

class DualHeap: 
    def __init__(self,k):
        self.small =[] #max heap
        self.large =[] #min heap
        self.delayed= Counter()
        self.k = k
        self.small_size = 0
        self.large_size = 0
        
    def prune(self, heap):
        while heap:
            num = -heap[0] if heap == self.small else heap[0]
            
            if self.delayed[num]:
                self.delayed[num] -=1
                heapq.heappop(heap)
            else:
                break
            
    def balance(self):
        if self.small_size > self.large_size + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
            self.small_size -=1
            self.large_size +=1 
            self.prune(self.small)
            
        elif self.small_size < self.large_size:
            heapq.heappush(self.small, -heapq.heappop(self.large))
            self.small_size +=1
            self.large_size -=1
            self.prune(self.large)
            
    def insert(self,num):
        if not self.small or num<=-self.small[0]:
            self.heappush(self.small , -num)
        else:
            heapq.heappush(self.large, num)
            self.large_size +=1
            
    def erase(self, num):
        
        self.delayed[num] +=1
        
        if num <= -self.small[0]:
          self.small_size -=1
          if num == -self.small[0]:
            self.prune(self.small)
        
        else:
            self.large_size -=1
            if num == self.large[0]:
              self.prune(self.large)
        
        self.balance()
        
    def median(self):
        if self.k % 2:
            return -self.small[0]
        
        return (-self.small[0] + self.large[0])/2
              
              
#Priority Queue Updates : 
import heapq

pq=[]
dist=[float('inf')] * n

dist[src] = 0
heapq.heappush(pq,(0,src))

while pq:
    d, node = heapq.heappop(pq)
    
    if d > dist[node]:
        continue
    
    for nei , w in graph[node]:
        nd = d + w
        
        if nd < dist[nei]:
            dist[nei] = nd
            heapq.heappush(pq, (nd, nei))
            

#Recoganization Pattern: 
# -> remove arbitary element from heap 
# -> update priority
# -> sliding window remove element
# -> dynamic removal

#Heapify Performance trick : use : heapq.heapify(arr) -> TC = O(n)
# for x in arr:
#     heappush(heap,x) -> TC = O(n log(n))

#Template
import heapq

class Heap:
    def __init__(self):
        self.h = []
        
    def push(self,x):
        heapq.heappush(self.h,x)
        
    def pop(self):
        heapq.heappush(self.h)
    
    def top(self):
        return self.h[0]
    
    def size(self):
        return len(self.h)
    
#Heap Problem Recoganisation Pattern 

#minimum element repeatedly
#top k
#priority selection
#merge sorted streams
#Use Heap 

# Problem  	        Example
# Top K     |     K largest elements
# Graph     |	  Dijkstra
# Greedy    |	  task scheduling
# Intervals |	  meeting rooms
# Merge     |	  merge k sorted lists
# Streaming |     median
# Priority  |     CPU scheduling

#Use Tuple Ordering Instead of custom comparator