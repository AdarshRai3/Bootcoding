#Core Template 
l,r = 0 , n-1

while l <=r:
    mid = (l+r)//2
    
    if arr[mid] == target:
        print(mid)
        break
    
    elif arr[mid]<target:
        l = mid + 1
    
    else:
        r = mid - 1

# Time Complexity : O(log(n))

#Pattern : 
#First True Pattern 
# Minimum capacity
# Minimum time
# Minimum distance
# Lower bound
l,r = 0 , n

while l<r:
    mid = (l+r)//2
    
    if check(mid):
        r = mid
    else:
        l= mid + 1
        
answer = l


#Pattern : Last True Pattern
#Upper Bound 
l,r = 0,n

while l<r:
    mid = (l+r)//2
    if check(mid):
       r = mid
    else:
       r = mid + 1
       
answer = l

# Binary Search on Answer
def check(x):
    pass 

l,r = 1 , 10**18

while l < r:
    mid = (l+r)//2
    
    if check(mid):
        r = mid
    
    else:
        l = mid + 1
        
print(l)

#Pattern : 
import bisect

#Find first postion >= target
bisect.bisect_left(arr,x)

#Find last postion >=target
bisect.bisect_right(arr,x)

#Count number of occurence 
count = bisect_right(arr,x) - bisect_left(arr,x)

#Pattern : Lower Bound (First True)
l, r = 0 ,n 

while l < r:
    mid = (l + r) //2 
    if arr[mid] >=x:
        r = mid
    else:
        l = mid + 1


# Pattern : Upper Bound(Last True)
l,r=0,n

while l<r:
    mid = (l+r)//2
    if arr[mid] >=x:
        r = mid
    else:
        l= mid + 1

#Search insert position 
bisect.bisect_left(arr,x)

#Kth smallest
# matrix sorted rows
# min(matrix)->max(matrix)

# Minimal Contest template 
l,r = 0,n
while l < r:
    mid (l+r)//2
    
    if condition(mid):
        r = mid
    else:
        l = mid+1
        
answer = l


def binary_search():
    l,r = 0,10**18
    
    while l<r:
        mid = (l+r)//2
        
        if check(mid):
            r=mid
        else:
            l=mid+1
    
    return l

    