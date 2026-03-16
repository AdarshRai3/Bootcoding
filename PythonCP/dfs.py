#Core Idea of DFS
# DFS explores a graph as deep as possible before backtracking.
# Conceptually:
# start node
#  → go to neighbor
#    → go deeper
#      → until no unvisited node
#        → backtrack

# Used for:
# connected components
# cycle detection
# topological sort
# tree traversal
# subtree DP
# grid problems
# articulation points / bridges

# Time complexity:
#     O(V + E)

# Competitive Graph Representation

from collections import defaultdict

n,m = map(int, input().split())

g= [[] for _ in range(n)]

for _ in range(m):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u) #remove it is directed 
    
# Why we use adjaceny list?
# *Memory Efficent
# *Fast iteration
# *Optimal for sparse graphs

# Classic Dfs is use recursion

import sys
sys.setrecusrsionlimit(10**7)

def dfs(node):
    visited[node] = True
    
    for nei in g[node]:
        if not visited[nei]:
            dfs[nei]
            
visited= [False] * n
dfs(0)

# Key ideas:
# visited prevents infinite loops
# recursion explores deep first

# Iternative DFS (stack version):
    
def dfs(start):
    stack = [start]
    
    while stack:
        node = stack.pop()
        if visited[node]:
            continue
        
        visited[node] = True
        
        for nei in g[node]:
            if not visited[nei]:
                stack.append(nei)
                
# Performance note:
# Iterative DFS is often faster and safer in Python contests.

# DFS Pattern 1 — Connected Components
def dfs(v):
    visited[v] = True
    for u in g[v] :
        if not visited[u]:
            dfs(u)

components = 0

for i in range(n):
    if not visited[i]:
        dfs(i)
        components +=1

# Use cases:
# number of provinces
# islands
# groups
# clusters

#DFS Pattern 2 : Cycle Detection(undirected)

# Key idea : Track Parent Node.

def dfs(v, parent):
    visited[v]=True
    for u in g[v]:
        if not visited[u]:
            if dfs(u,v):
                return True
        elif u != parent:
            return True
        
    return False

# Used 
# Detects cycles in:
# undirected graphs
# tree validation problems

#DFS Pattern 3- Cycle Detection(Directed)

# Use 3-state visited array

# 0 = unvisited 
# 1 = visiting
# 2 = done

def dfs(node):
    start[node] = 1
    
    for u in g[node]:
        if state[u] == 1:
            return True
        
        if state[u] == 0:
            if dfs(u):
                return True
    
    state[v] = 2
    return False

#Used in 
# course schedule
# DAG validation
# dependency graphs 

# Pattern : 4 : Topological Sort 
# DFS + postorder stack.
def dfs(v):
    visited[v] = True
    
    for u in g[v]:
        if not visited[u]:
            dfs(u)
    
    order.append(v)
    
for i in range(n):
    if not visited[i]:
        dfs(i)

order.reverse()

# Pattern 5 : Grid DFS
# Very Command in contest
# Example: Number of Island

dirs=[(1,0),(-1,0),(0,1),(0,-1)]

def dfs(r,c):
    stack=[(r,c)]
    
    while stack:
        x,y = stack.pop()
        
        if visited[x][y]:
            continue
        
        visited[x][y] = True
        
        for dx,dy in dirs:
            nx , ny = x+dx , y+dy
            
            if 0<=nx<n and 0<=ny<m and grid[nx][ny] == 1:
                stack.append((nx,ny))
                
#Pattern6 : Tree DFS:

def dfs(v, parent):
    size[v] = 1
    
    for u in g[v]:
        if u != parent:
            dfs(u,v)
            size[v] += size[u]

#Used in:
# subtree sums
# DP in trees 
# rerooting problems      

#Performance Trick 

# Increase recursion limit
import sys
sys.setrecursionlimit(10**7)  

#Use adjaceny list not dict
g=[[] for _ in range(n)]

#Template 
import sys
input = sys.stdin.readline
sys.setrecusrsionlimit(10**7)

n,m = map(int, input().split())

g=[[] for _ in range(n)]

for _ in range(m):
    u,v = map(int, input().split())
    u -=1 
    v -=1
    g[u].append(v)
    g[v].append(u)
    
visited[False]*n

def dfs(v):
    visited[v] = True
    for u in g[v]:
        if not visited[u]:
            dfs(u)
            
for i in range(n):
    if not visited[i]:
        dfs(i)
        
        
# Advanced DFS Patterns 

# You should also know:
    
# Technique	            Used For
# Euler Tour	            subtree queries
# DFS timestamps	        ancestor queries
# Low-link values	        bridges/articulation points
# DFS order flattening	segment tree on tree
# DP on tree	            rerooting


#Euler Tour Technique(Flattening a tree)

import sys 

sys.setrecursionlimit(10**7)

timer=0
tin =[0]*n
tout=[0]*n
order=[0]*n

def dfs(v,p):
    global timer
    tin[v] = timer
    order[timer] = v
    timer +=1
    
    for u in g[v]:
        if u != p:
            dfs(u,v)
    
    tout[v] = timer-1
    
# Now subtree of v = 
# [tin[v], tout[v]]

# Used for: 
#     subtree sum queries
#     subtree updates
#     tree + segment tree

#Diameter = longest path in tree
# DFS from any node -> farthest node A
# DFS from A -> farthest node B
# distance(A,B) = Diameter
def dfs(v,p,d):
    far = (d,v)
    
    for u in g[v]:
        
        if u != p:
            cand=dfs(u,v,d+1)
            
            if cand[0] > far[0]:
                far = cand
    
    return far

_,a = dfs(0,-1,0)

diameter,b = dfs(a,-1,0)

# TimeComplexity : O(N)

# Used in:
# tree distance problems
# CF tree problems
# network delay style tasks

#Low - Link Value (Bridges)

# A bridge is an edge whose removal discoonets the graph

# DFS computes two value 

# tin[v] -> discovery time
# low[v] -> earliest reachable ancestor

# Bridge Condition:
#     low[to] > tin[v]

timer = 0
tin = [-1]*n
low = [-1]*n

def dfs(v,p):
    global timer
    tin[v] = low[v] = timer 
    timer +=1
    
    for to in g[v]:
        if to == p:
            continue
        
        if tin[to] != -1:
            low[v] = min(low[v], tin[to])
            
        else:
            dfs(to,v)
            low[v] = min(low[v] , low[to])
            
            if low[to] > tin[v]:
                print(b"bridge" ,v,to)
                
# Used in:
# bridge detection
# articulation points
# network resilience problems

# Articulation Points:
# A vertex that disconnects the graph when removed

# Condition: 
# low[to] >= tin[v]

# Special case for root

def dfs(v,p):
    children = 0
    tin[v] = low[v] = timer
    
    for to in g[v]:
        if to == p:
            continue 
        
        if tin[to] != -1:
            low[v] = min(low[v], tin[to])
            
            if low[to]>=tin[v] and p!=-1:
                print("articulation:" ,v)
                
                children +=1
                
    if p == -1 and children > 1:
        print('articulation:', v)
        
# Tree DP (subtree dp)

sub =[0]*n

def dfs(v,p):
    sub(v) =1
    
    for u in g[v]:
        if u!= p:
            dfs(u,v)
            sub[v] += sub[u]
        
        

