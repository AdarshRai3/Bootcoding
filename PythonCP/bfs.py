#BFS is generally focused and used in unweighted graph 
#Template 
from collections import deque

def bfs(start,graph,n):
    q = deque([start])
    visited = [False]*n
    visited[start] = True
    
    while q : 
        node = q.popleft()
        
        for nei in graph[node]:
            if not visited[nei]:
                visited[nei] = True
                q.append(nei)
                
#6 line Bfs (Grandmaster):
from collections import deque

q = deque([s])
dist=[-1]*n
dist[s] = 0

while q:
    v=q.popleft()
    for u in g[v]:
        if dist[u]<0:
            dist[u] = dist[v] + 1
            q.append(u)
            
# dist<0 = not visited
# distance + visited in one array
# minimal branching

# Pattern 1 — Shortest Path in Unweighted Graph
# Idea
# Each edge weight = 1 → BFS guarantees shortest distance.

from collections import deque

def bfs(start):
    q = deque([start])
    dist=[-1]*n
    dist[start] = 0
    
    while q:
        v = q.popleft()
        
        for u in g[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                q.append(u)
                
    return dist

#Used in : Message Route , Shortest path in unweighted graph

# Pattern 2 — BFS on Grid
# dirs = [(1,0),(-1,0),(0,1),(0,-1)]

from collections import deque

def bfs(sx,sy):
    q = deque([sx,sy])
    dist = [[-1]*m for _ in range(n)]
    dist[sx][sy] = 0
    
    while q:
        x,y = q.popleft()
        
        for dx, dy in dirs:
            nx,ny = x+dx ,y+dy
            
            if 0<=nx<x and 0<=ny<m and dist[nx][ny] == 1:
                dist[nx][ny]=dist[x][y] + 1
                q.append((nx,ny))
                
#Classic Problems
# Labyrinth
# Rotting Oranges

# 3. Pattern 3 — Multi-Source BFS
# Push many starting nodes at once.

from collections import deque

q = deque
dist = [-1] * n

for s in sources:
    q.append(s)
    dist[s] = 0
    
while q:
    v = q.popleft()
    
    for u in g[v]:
        if dist[u] == -1:
            dist[u] = dist[v] + 1
            q.append(u)

#Monsters


# Pattern 4 — BFS with Parent Reconstruction
# Used when problem asks for path output.
# Example: print path from A → B.

parent = [-1]*n

while q:
    v = q.popleft()
    
    for u in g[v]:
        if dist[u] == -1:
            dist[u] = dist[v] + 1
            parent[u] = v
            q.append(u)
        
# Path reconstruction:
path = []
cur = target

while cur != -1:
    path.append(cur)
    cur = patent[cur]
    
path.reverse()

# Pattern 5 — BFS With State
# (node, mask)
# (node , energy)
# (x,y , keys)

from collections import deque

q = deque([start,0])
visited = set([(start,0)])

while q:
    node, mask = q.popleft()
    
    for nxt in transition(node, mask):
        if nxt not in visited:
            visited.add(nxt)
            q.append(nxt)
            
#Used in visiting all nodes , key door problems , bitmask BFS

# Pattern 6 — 0-1 BFS

from collections import deque

dq = deque([start])

dist=[10**18]*n
dist[start] = 0

while dq:
    v = dq.popleft()
    
    for u,w in g[v]:
        if dist[v] + w < dist[u]:
            dist[u] = dist[v] + w
            
            if w == 1:
                dq.append(u)
            else:
                dq.appendleft(u)
                
# 7. Pattern 7 — BFS on Implicit Graph
# Graph is not explicitly given.  

from collections import deque

q = deque([start])
visited = set([start])

while q:
    x = q.popleft()
    
    for nx in [x-1,x+1,x*2]:
        if nx not in visited and valid(nx):
            visited.add(nx)
            q.append(nx)

# Used For : Minimum Operation to transform Number

#Performance

g=[[] for _ in range(n)] #Correct way
matrix = [[0]*n]*n

# (Avoid set when possible)
visited = [False]*n

#Avoid tuple allocation in hot loops
q.append((x,y))

id = x*m + y

x = id/m
y = id%m

#Predefine direction once
DIRS=((1,0),(-1,0),(0,1),(0,-1))
# BFS Recorginsation:
# minimum moves
# shortest path
# unweighted graph
# grid movement
# spreading process
# layers
# levels

#Faster Shortest Path(BFS):
#Bidirectional BFS

from collections import deque

def bidirectional_bfs(start, target, graph):
    q1=deque([start])
    q2=deque([target])
    
    dist1={start:0}
    dist2={target:0}
    
    while q1 in q2:
        
        v = q1.popleft()
        
        for u in graph[v]:
            if u not in dist1:
                dist1[u] = dist1[v] + 1
                q1.append(u)
                
                if u in dist2:
                    return dist1[u] + dist2[u]
                
        v = q2.popleft()
        
        for u in graph[v]:
            if u not in dist2:
                dist2[u] = dist2[v] + 1
                q2.append(u)
                
                if u in dist1:
                    return dist1[u] + dist2[u]
        
        return -1

# BFS + Bitmask (Hard Graph Problems)
# Used when we must visit many nodes and track visited subset.
# State:
# (node, mask)
# Mask represents visited nodes.

from collections import deque

def bfs():
    q=deque([start,1<<start])
    visited = set([(start,1<<start)])
    
    while q:
        node,mask = q.popleft()
        
        if mask == (1<<n)-1:
            return
        
        for nei in g[node]:
            new_mask = mask | (1<<nei)
            
            state = (nei,new_mask)
            
            if state not in visited:
                visited.add(state)
                q.append(state)
                
#Shortest path visiting all nodes 
#Time Complexity : O(n*2^n)
#Works when n<= 15

#Graph Compression

#Graph compression in BFS

# Sometimes graph size is too large to explictly build
# n=1e9

# Idea : 
# Create Neighbour on the fly

from collections import deque

def bfs(start,target):
    
    q=deque([start])
    visited = set([start])
    
    while q:
        x=q.popleft()
        for nx in [x-1,x+1,x*2]:
            if nx not in visited and 0<=nx<=limit:
                visited.add(nx)
                q.append(nx)
                
#Minimum Operations to transform a number

#BFS on Tree

# Tree are a special case of graph
edges = nodes -1 
# Problem we can apply:
    # compute depth
    # find farthest node 
    # tree diameter
    
from collections import deque 

def bfs(start):
    q=deque([start])
    dist = [-1]*n
    dist[start]=0
    
    while q:
        v = q.popleft()
        
        for u in g[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                q.append(v)
                
    return dist

# Tree Diameter Trick:
#     two Bfs runs:
        
BFS Layer Processing

while q : 
    size = len(q)
    
    for _ in range(size):
        node = q.popleft()
        for nei in g[node]:
            q.append(nei)
            
# Used in : Time passes in each level
# Problems:
# Infection Spreed
# Burning Tree
# Rotting Oranges

#6 MultiSource Bfs : 
# run one BFS with multiple sources

q = deque()

for i in range(n):
    if grid[i] == 'H':
        q.append(i)
        dist[i] = 0
        
# BFS + Parent Tracking:
parent = [-1]*n

while q:
    v = q.popleft()
    
    for u in g[v]:
        
        if dist[u] == -1:
            dist[u] = dist[v] + 1
            parent[u] = v
            q.append(u)
            
            
path = []
cur = target

while cur != -1:
    path.append(cur)
    cur = parent[cur]

path.reverse()

#BFS optimisation trick 

# Trick 1 : Combine visited + distance
#Instead of 
visited + dist arrays

# Use only
dist == -1

# Trick 2 - Avoid Tuple Overhead
# Instead of :
#     q.append((x,y))
# Use encoding :
#     id = x*m + y 
# decoding:
#     x = id//m
#     y = id%m

#Trick3 : Prelocating arrays

dist=[-1]*n

# Trick:4 : Adjacency List
g=[[] for _ in range(n)]

#Recoganise BFS Problem Quickly
# minimum moves
# shortest path
# unweighted graph
# grid movement
# spreading process
# levels
# fewest steps
