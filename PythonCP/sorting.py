a = [5, 2, 9,1]
a.sort() #in-place
b = sorted(a) #new list


#Reverse sort 
a.sort(reverse=True)

#sorting with key
a.sort(key = lambda x:x[1])

#sort by absolute value
#sort by abs
a.sort(key=abs)
#sort by second element
a.sort(key=lambda x:x[1])
#sort by multiple key
a.sort(key=lambda x:(x[0], -x[1]))

#Multikey sorting 
#primary ascending , secondary descending
a.sort(key = lambda x:(x[0],-x[1]))

#To keep original position
arr = [40,10,30]
idx = sorted(range(len(arr)), key=lambda i :arr[i])

#Co-ordinate compression
vals = sorted(set(arr))
comp = {v:i for i,v in enumerate(vals)}
compressed =[comp[x] for x in arr]

#Custom comparator
from func_tool import cmp_to_key

def cmp(a,b):
    if a[0] == b[0]:
        return b[1]-a[1]
    return a[0]-b[0]

arr.sort(key = cmp_to_key(cmp))

#Pattern:1
#Sorting by freq
from collections import Counter
cnt = Counter(arr)
arr.sort(key = lambda x:(cnt[x],x))

#Sort Stable Trick 
arr.sort(key=lambda x:x[1])

arr.sort(key=lambda x:x[0])
#works because stability preserve order 


#Pattern:2
#Sorting pattern in Codeforces 
"Sort-> Linear Pass"
arr.sort(key = lambda x:x[1])
last = -10**18
count = 0

for l,r in arr:
    if l >= last:
        count +=1
        last = r
        
#Sorting Pairs for inequality transform 
#Instead of checking inequality in the a[i] + a[j] > a[k]4
#Sort first

#Pattern 3 sort + two pointers 
n=len(arr)
arr.sort()
l,r =0, n-1

while l<r:
    if arr[l] + arr[r] < target
        l+=1
    else:
        r-=1


#Pattern:4
"Sort with difference (Classic 2200-2500)"
arr.sort(key=lambda x:x[0]-x[1])

#Pattern:5
"Sort in descending order"
arr.sort(reverse=True)

#Pattern:6
pairs = [(value, index)]
pairs.sort()

ans=[0]*n

for i , (_,idx) in enumerate(pairs):
    ans[idx]+=1
    

arr.sort(key=lamdba x :expensive_function(x)) #slow
val =[expensive_function(x) for x in arr]
arr =[x for _,x in sorted(zip(vals,arr))]


arr.sort(key=lambda x:x.bit_count())

#Sort by parity
arr.sort(key= lambda x:(x%2,x))

#largest concatenated number 
from functools import cmp_to_key

def cmp(a,b):
    if a+b > b+a: return -1
    if a+b < b+a: return 1
    return 0

arr.sort(key=cmp_to_key(cmp))

#Partial Sorting 
import heapq
largest_k = heapq.nlargest(k,arr)

