from collections import deque

dq = deque()

#push
dq.append(x)  #push right
dq.appendleft(x)  #push left

#pop
dq.pop() #remove right
dq.popleft() #remove left

#access
dq[0] #front
dq[-1] #back

#length
len(dq)

#clear
dq.clear()

dq = deque([1,2,3])
dq = deque(maxlen = 5) #fixed size queue

#Queue in BFS : Pattern 1 : 
from collections import deque

def bfs(start):
    q = deque([start])
    visited = set([start])
    
    while q:
        node = q.popleft()
        
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append(nei)
                
# Using Deque is important Bfs requires FIFO operations

#Pattern 2 :Sliding window 

#Used for maintaining window

from collections import deque

dq = deque()

for i in range(n):
    dq.append(arr[i])
    
    if len(dq) > k:
        dq.popleft()
        
    if len(dq) == k:
        process(dq)
        

#Pattern 3 Monotonic Queue
from collections import deque

dq = deque()
res = []

for i in range(len(nums)):
    while dq and nums[dq[-1]] < nums[i]:
        dq.pop()
    
    dq.append(i)
    
    if dq[0] <= i-k:
        dq.popleft()
        
    if i>=k-1:
        res.append(nums[dq[0]])
        
#Deque stores indices in decreasing order
# Time Complexity : O(n)


#Pattern 4 -0-1 BFS

# Used in graphs where edges are 0 or 1. Instead of Dijkstra

from collections import deque

dist=[float('inf')] * n
dist[src] = 0

dq = deque([src])

while dq:
    node = dq.popleft()
    
    for nei, w in graph[node]:
        if dist[node] + w < dist[nei]:
            dist[nei] = dist[node] + w
            
            if w == 0:
                dq.appendleft(nei)
                
            else:
                dq.append(nei)
                
#Time complexity : O(V+E)
#This is faster for this case than Dijkstra

# Maintain Increasing / Decreasing Structure
while dq and dq[-1] >x:
    dq.pop()
    
dq.append(x)

# Used in : Dp Optimisation , Monotonic Queue and convex hull trick varaitions

#Performance :

#Always store indices not values 
# dq.append(nums[i]) -> Incorrect
# dq.append(i) ->Correct

#Avoid converting dq to list the cost of conversion is O(N)-> list(dq)


#Contest template : 
from collections import deque

dq = deque()

dq.append(x)
dq.appendleft(x)

dq.pop()
dq.popleft()

front = dq[0]
back  = dq[-1]

#Key due to deque most algorithm time complexity reduce from O(n log n)-> O(n)