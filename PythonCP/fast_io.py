"""input() vs sys.stdin.readline()"""
n = int(input())

import sys
n = int(sys.stdin.readline())

"""
Why it is fast?
input() internally use stripe()+additional_check() which slow down
"""

import sys 
input= sys.stdin.readline

def solve():
    n = int(input())
    arr=list(map(int,input().split()))
    print(sum(arr))
    
if __name__ = "__main__":
    solve()
    
""" 
Even Faster : Bulk Read Strategy:
For extreme input of size(10^6+ numbers)
"""
import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    
    n = int(data[idx]);idx+=1
    arr = list(map(int, data[idx:idx+n]))
    idx += n
    
    print(sum(arr))
    
if __name__ == "__main__":
    solve()
    
"""
Why this is the fastest?
Only one system call
No repeated .readline()
Split once
Iterate via index pointer
"""

"""
Fast Output
Print vs Buffered write
"""
for x in arr:
    print(x)
    

import sys
output = []
for x in arr:
    output.append(str(x))

sys.stdout.write("\n".join(output))
"""
Why?
print() flush logic
Each call expensive
joining once is O(n)
"""

"""
Parsing Pattern we need to memorize
"""
"""Basic Scalar"""
""" Integer"""
n = int(input())
""" Float"""
n = float(input())
"""String"""
n = input().stripe()
#-----------------------------------------------------
"""Multiple Values"""
""" Multiple ints"""
a, b = map(int, input().split())
a, b,c = map(int, input().split())
n,s = input().split()
n = int(n)
#-----------------------------------------------------
"""List Parsing"""
"""List of int"""
arr = list(map(int, input().split()))
arr = list(map(float, input().split()))
arr = [int(x)-1 for x in input().split()]
#-----------------------------------------------------
"""Grid Parsing"""
"""Matrix Input"""
n, m = map(int, input().split())
"""
a b c
d e f
g h i
"""
n = int(input())
grid = [list(input().strip())for _ in range(n)]
"""
3 4 
1 2 3 4
5 6 7 8
9 10 11 12
"""
n , m = map(int,input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

"""Multiple Test Cases"""
t = int(input())
for _ in range(t):
    solve()

data = sys.stdin.read().split()
idx = 0
t = int(data[idx]); idx+=1

for _ in range(t):
    n = int(data[idx]); idx+=1
    
"""Edge List(Graph)"""
"""undirected Graph"""
n,m = map(int,input().split())
adj =[[] for _ in range(n)]

for _ in range(m):
    u,v = map(int, input().split())
    u-=1;v-=1
    adj[u].append(v)
    adj[v].append(u)
    
"""weighted graph"""
n,m = map(int, input().split())
adj = [[] for _ in range(n)]

for _ in range(m):
    u,v,w = map(int, input().split())
    u-=1; v-=1
    adj[u].append((v,w))
    adj[v].append((u,w))

"""Parent Array (tree)"""
n = int(input())
parents = list(map(int, input().split()))

"""Reading  until EOF"""
import sys 

for line in sys.stdin:
    process(line.strip())
    
"""Bulk Parsing a large input"""
import sys

data = sys.stdin.read().split()
idx = 0

n = int(data[idx]); idx+=1
arr = list(map(int, data[idx:idx+n]))
idx+=n

"""Binary Parsing"""
s=input().strip()
bits= [int(c) for c in s]

"""Query"""
q= int(input())
for _ in range(q):
    query = input().split()
    if query[0] == "1":
        x = int(query[1])
        y = int(query[2])
    else:
        x = int(query[1])
        
"""Tuple(Immutable)"""
n = int(input())
points = [tuple(map(int,input().split())) for _ in range(n)]

""" Compressed Single Line input"""
data = list(map(int,input().split()))
k = data[0]
arr = data[1:]

"""Blank line in input"""
while True: 
    line = input().strip()
    if not line: 
        break
    
"""Strip vs Split vs Replace"""
"""Strip remove character from start and end of the """
"""Strip : Use when we want to read string without white-space with lstrip and rsripe to remove left and right specifically"""
"""Split : Use when we want to convert a give input in form of continuous string or number to individual input in our list"""
"""Replace : It take two argument and remove character from anywhere"""

"""String Parsing"""
s = input().strip()

#String is immutable when we want to change the string in-place we convert string into List which is mutable and allow inplace modification
chars = list(s)

#When we want to read string char in ascii/unicode value
vals =[ord(c) for c in s]

#Convert digit string into integer list
digits = list(map(int,s))

#Properties
len(s)
s[0]
s[-1]
s.lower()
s.upper()

#Iteration
for c in s:
    ...
#With index: 
for i,c in enumerate(s):
    ...

for c in reversed(s):
    ...

#Operations
"Lexographical comparision is built-in"
if s < t : 
    ... 
    
"Reverse String"
rev = s[::-1]

"Palindrome Check"
is_pal = (s == s[::-1])

"Frequency counting"
freq = {} 
for c in s : 
    freq[c] = freq.get(c,0)+1

"Using counter"
from collections import Counter
freq = Counter(s)

    
"Lowercase Freqency Counter"
freq = [0]*26
for c in s : 
    freq[ord(c)-ord('a')]+=1
    
"""substing check """
for "abc" in s:
    ...

"""Count substring"""
count = s.count("abc")

"""split pattern"""
words = input().split()

parts = input().split(",")

"join pattern"
list_of_strings=[]
result = "".join(list_of_strings)

res = [] 
for c in s:
    res.append(c)
final = "".join(res)

sorted_s = ''.join(sorted(s))

"""Replace Pattern"""
s = s.replace("a" , "*")

"""Two Pointer Pattern"""
i=j=0
while i<len(s) and j<len(t):
    if s[i] == t[j]:
        j+=1
    i+=1
is_subsequence = (j==len(t))
"""Prefix Sum"""
n = len(s)
prefix = [[0]*26 for _ in range(n+1)]

for i in range(n):
    for j in range(26):
        prefix[i+1][j] = prefix[i][j]
    
    prefix[i+1][ord(s[i]-97)] +=1
    
freq=prefix[r+1][c] - prefix[l][c]

"""Performance"""
#I/O cost heiracrhy
"System Call >> Python Function Call >> Python Loop >> arthimetic"
"""
Map is faster than list comphrension because : 
Map run loop in c vs list comphrension run loop in Python Bytecode
Reason : Fewer Python level operation + Lower intrepretor overhead

Local variables are faster than Global variable
Local requires Fast local array (C array lookup) 
Gloabl requires Dictionary Lookup (Load_Global)


"""