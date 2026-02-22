"""Operations"""
"""
a[i] -> O[1] : True constant time
a.append(x) -> Amortized O(1) -> Ocassioal Resizing takes time where list grow from 1.125 to 1.5x 
a.pop->O(1) -> From end only
a.pop(i)->O(n)->Shift cost
a.insert(i,x) -> O(n) -> shift right
del a[i] ->O(n)->Shift left
a.sort()->O(nlogn)->TimSort
x in a -> O(n)-linear scan
a + b -> O(n+m) -> New list allocated
a *k -> O(k*n)-> Repeated Reference
"""

"Preallocation"
"If you know the size this is best way"
a =[0] * 26 #Best
a = [] #Poor
for i in range(n):
    a.append(i)

"Reason: Best run on single c loop where as poor runs of python bytecoder which increase intrepretor overhead"""
n=int(input())
a=[]
for i in range(n):
    a.append(i*i) #slow : Python byte code per append

a = list(map(lambda i : i*i , range(n))) #Faster : Reason it requires python function call due to use of lambda in data manipulation , for read case it is faster than list comphrension
a = list(map(abs,a))#In this case map is faster than list compherension 
a = [abs(x) for x in a]
a = [i*i in i in a] #Fastest : Single c-loop

"""Avoid repeated membership check"""
x = "Test"
if x in a : 
  pass  
#if frequent-> use set
s = set(a)
if x in s:
    pass

#Reduces from O(n) to O(1) as set use internally hashing which make checking faster

"""Avoid pop[0]"""
from collections import deque
dq= deque()
dq.popleft()

"""Avoid List Concatenation in Loop"""
#If you add with concatination it will create new memory which 
res = []
chunks=[]
for chunk in chunks:
    res+= chunk #Slower
    
res.extend(chunk)#Faster

from itertools import chain
res = list(chain.from_iterable(chunks))
    
#Avoid Repeated Silicing use window with index
for i in range(n):
    temp = a[i:i+3] #slow
    
window_sum= a[0] + a[1] + a[2]

for i in range(3,n):
    if window_sum == target:
        pass
    
    window_sum += a[i]
    window_sum -= a[i-3]
    
#generic 
k=5
window_sum = sum(a[:k])
    
for i in range(k,n):
    if window_sum == target:
        pass
    
    window_sum +=a[i]
    widow_sum -= a[i-k]
    
"""Sorting"""
from functools import cmp_to_key
a.sort(key=cmp_to_key(mycmp))
#Comparator -> heavy python calls

a.sort(key=lambda x:x[1])
#key function -> computated once per element

"""Decorate-sort-undecorate(Schwartzian)"""
a = [(key(x),x) for x in a]
a.sort() 
a[x[1] for x in a ]


    
# List is contigous and cache friendly.
"Better"
for x in a: 
    pass

for i in range(len(a)):
    x=a[i]
    
'''Micro-optimisation'''
append = a.append

for i in range(n):
    append(i)
    
'''Avoid global lookup'''
from sys import stdin
input=stdin.readline()

'''Avoid nested python loope when possible'''
'''List as stack'''
stack =[]
stack.append(x)
stack.pop()

#List Copy Pitfall
b=a[:]
b=list(a)
b=a.copy() #this will create a new list space in memory only ptr get copied

b=a
# in this you are using the same list

#if you want create a entirely new list with new with new pointer use deepcopy 
import copy
b = copy.deepcopy(a)

#Important!
a=[[0]*m]*n #Incorrect

a=[[0]*m for_ in range(n)]

#Competative Patterns 
pref = [0]*(n+1)
for i in range(n):
    pref[i+1] = pref[i] + a[i]
    
diff = [0]*(n+1)
diff[l] +=x
diff[r+1] -=x

vals= sorted(set(a))
index = {v:i for i,v in enumerate(vals)}


    
    







