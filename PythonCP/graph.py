#Graph Representation
#Adjacency List
from collections import defaultdict

n=5
graph =[[] for _ in range(n)]

#source , destination
edges =[(0,1),(1,2),(2,3),(3,4)]

for u,v in edges:
    graph[u].append(v)
    graph[v].append(u)


#Adjacency List

graph =[[] for _ in range(n)]

edges =[(0,1,4),(1,2,7)]

for u,v,w in edges:
    graph[u].append((v,w))
    graph[v].append((u,w))
    
# Performance:
#     list adjacency list -> fastest
#     avoid dict unless node lables are large
#     memory:O(V+E)

#DFS Pattern
#Used for : 
# connected components
# cycle detection
# tree problems 
# graph coloring
# topological sort(DFS versions)

import sys
sys.setrecursionlimit(10**7)

def dfs(u,parent):
    visited[u] = True
    
    for v in graph[u]:
        if v == parent:
            continue
        
        if not visited[v]:
            dfs(v,u)
            
visited = [False]*n
dfs(0,-1)

# Time Complexity:
#     O(V+E)

#Use : Unweighted Graph with all weight = 1

# BFS Pattern (Shortest Path Unweighted)
from collections import deque

def bfs(start):
    q=deque([start])
    dist[start]=0
    
    while q:
        u = q.popleft()
        
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)

dist = [-1]*n
bfs(0)

# Time Complexity(O(V+E))

# use bfs when: 
    
# minimum edges path
# grid shortest path
# multi source BFS

#Dijkstra(Weighted Shortest Path):

# Use: Weighted Graph with not negative weight but graph with cyclic

import heapq

INF = 10**18
dist = [INF]*n
dist[0]=0

pq = [(0,0)]

while pq:
    d,u = heapq.heappop(pq)
    
    if d > dist[u]:
        continue
    
    for v,u in graph[u]:
        nd = d + w
        
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq,(nd,v))
            
# Time Complexity = O((V+E) log V)
#Use when : 
# Weighted Graph
# Positive Weight 
# Shortest Weight

#Topological Sort(DAG): Kahn's Algorithm
#Used when : 
# Directed Acyclic Graph
# Dependency ordering
#Example Problems:
# Course Schedules
# Build Order
# DP on DAG

from collections import deque

indegree=[0]*n

for u in range(n):
    for v in range(u):
        indegree[v]+=1
        
q = deque()

for i in range(n):
    if indegree[i] == 0:
        q.append(i)
        
order = []

while q:
    u = q.popleft()
    order.append(u)
    
    for v in graph[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            q.append(v)
            
# Time Complexity : O(V+E)

# Union-Find(Disjoint Set)

# Used when : 
# dynamic connectivity
# cycle detection
# MST

parent = list(range(n))

rank =[0]*n

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    ra,rb = find(a) , find(b)
    
    if ra == rb:
        return False
    
    if rank[ra] < rank [rb]:
       parent[ra] = rb
    else:
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] +=1
            
    return True

# Time complexity : O(Alpha(n))~Constant

#MInimum Spanning Tree 
# Krusal (union find)

# Preferred when : 
#     edges list given
#     sparse graph

edges.sort(key = lambda x:x[2])

cost = 0

for u,v,w in edges:
    if union(u,v):
        cost +=u
        
# Time Complexity : O(E log E)

#Grid Graph Pattern 

dirs=[(1,0) ,(-1,0) ,(0,1),(0,-1)]

for dx , dy in dirs:
    nx = x + dx
    ny = y + dy

# Used in : 
# Island Problems 
# Shortest Path
# Flood Fill

#Multi Source BFS

#Used When 
#Multiple starting nodes
#Rotting Oranges 

q = deque()

for i in range(n):
    if source[i]:
        q.append(i)
        dist[i]=0