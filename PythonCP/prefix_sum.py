#prefix sum 
#Core Idea : Calculate the sum once and then store it to use later for future calculation and quries
# Prefix sum stores the total up to each index so you can subtract and get any range instantly.
#Standard :
n=len(a)

pre = [0]*(n-1)

for i in range(n):
    pre[i+1] = pre[i] + a[i]
    
    
#Range Quries:
def range_sum(l,r):
    return pre[r+1]-pre[l]

#CP shortcut
from itertools import accumulate 

pre=[0] + list(accumulate(a))
#This is preferred as accumulate-> implementation -> faster

#Pattern : Range Sum Queries
#O(n+q)
pre = [0]

for x in a:
    pre.append(pre[-1]+x)
    
for _ in range(q):
    l,r = map(int,input().split())
    print(pre[r]-pre[l-1])

#Pattern : Count Subarrays With Given Sum
# prefix[j]-prefix[i] = k
# prefix[j] = k + prefix[i]

from collections import defaultdict

count=defaultdict(int)
count[0] = 1

pre=0
ans=0

for x in a:
    pre +=x
    ans += count[pre-k]
    count[pre] +=1
    
#Pattern 3 
# (prefix[j] - prefix[i]) % k = 0
# prefix[j] % k == prefix[i] % k

from collections import defaultdict

count =defaultdict(int)

count[0]=1

pre = 0
ans = 0

for x in a:
    pre = (pre + x)%k
    ans += count[pre]
    count[pre] +=1
    
# Pattern : Difference Array (Range Updates)
# diff[l] += x
# diff[r+1] -= x
# prefix sum to rebuild array

diff = [0]*(n-1)


for l,r,x in queries:
    diff[l] +=x
    diff[r+1] -=x

for i in range(1,n):
    diff[i] += diff[i-1]
    
    
# Pattern : Prefix Maximum/Minimum
# max subarray with constraint
# prefix[i] - minimum prefix before 
#Basically this is nothing but kadanes alogrithm 
pre = 0
min_pre = 0
ans = -10**18

for x in a:
    pre +=x 
    ans = max(ans,pre - min_pre)
    min_pre = min(min_pre,pre)

# Pattern 6 — 2D Prefix Sum
# For matrix queries : sum of rectangle
# Formula:pref[x2][y2]- pref[x1-1][y2]- pref[x2][y1-1]+ pref[x1-1][y1-1]

pre = [[0]*(m-1) for _ in range(n+1)]

for i in range(n):
    for j in range(m):
        pre[i+1][j+1] = (a[i][j] + pre[i][j+1] + pre[i+1][j] - pre[i][j])
        
#Context ready template: 
import sys
input = sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))

pre=[0]*(n+1)

for i in range(n):
    pre[i+1] = a[i]+pre[i]
    
def query(l,r):
    return pre[r+1]-pre[l]

