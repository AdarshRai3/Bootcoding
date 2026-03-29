# Two Pointers = using indices to scan intelligently intead of nested loops 

# for i : 
#     for j :

# i = 0
# j = n-1 
# while condition:
#     move i or j smartly

# Goal reduce O(n^2)->O(n)

# Pattern : 1 : Converging Pointers(Opposite Ends)
# Use case : Sorted Array , Find Pair/triplet , Min/Max constraints

def two_sum(arr, target):
    i,j = 0 , len(arr)-1
    
    while i<j:
        s = arr[i] + arr[j]
        
        if s == target:
            return (i,j)
        elif s < target:
            i +=1
        else:
            j-=1
        
    return -1

# Pattern Rule:
#     Too small -> move left pointer
#     Too big   -> move right pointer

# Pattern 2 : Same Direction(Fast and Slow Pointer)
# Use Case
    Remove Duplicates
    Parition Array
    In place modication
    
def remove_duplicates(arr):
    i=0
    
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i +=1 
            arr[i] = arr[j]
            
    return i+1

# Pattern Rule
# i-> last unique position
# j->scanning pointer

# Pattern 3 : Sliding Window
# Use Case : Subarray / substring
# Max/min length
# Sum constraints

def longest_unique(s):
    seen = set()
    
    l = 0
    res = 0
    
    for r in range(len(s)):
        while s[r] in seen:
            seen.remove(s[l])
            l+=1
            
        seen.add(s[r])
        res = max(res, r-l+1)
    
    return res

# Pattern Rule
# Expand r++
# Violation shrink l++

# Pattern 4 Ductch national Flag:
#     Rearranging array
#     0,1,2s
#     Quicksort partition logic

def sort_colors(nums):
    low, mid , high = 0 , 0 ,len(nums)-1
    
    while mid <= high:
        if nums[mid] ==0:
            nums[low],nums[mid] = nums[mid],nums[low]
            low+=1
            mid+=1
        elif nums[mid]==1:
            mid+=1
        else:
            nums[mid],nums[high] = nums[high],nums[mid]
            high -=1

# Pattern Rule:
# Maintain Regions
# [0 → low-1] = 0
# [low → mid-1] = 1
# [high+1 → end] = 2
        
# Pattern 5: Cycle Detection(floyd algorithm)
# Use case:
#     Linked List cycle 
#     Fast/slow pointer trick
    
def has_cycle(head):
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
        
    return False
    
    
# Pattern 6:K-Sum(Extension)
#Use Case
# 3sum/4sum

# Idea : Fix one element and apply two pointer

def three_sum(nums):
    nums.sort()
    res = []
    
    for i in range(len(nums)):
        l,r = i+1,len(nums)-1
        
        while l < r:
            s = nums[i] + nums[l] + nums[j]
            
            if s == 0:
                res.append([nums[i],nums[l],nums[r]])
                l+=1
                r-=1
            elif s < 0:
                l+=1
            else:
                r-=1
                
# Recoganisation Cheat Sheet:
#     Sorted Array + Pair/Triplet -> Opposite Pointers
#     Remove duplicates / in-place -> Fast & slow
#     Subarray/SUbstring -> Sliding window
#     Rearrange elements -> Partition
#     Linked list cycke -> Fast/slow
#     Triplets/quadruplets -> K-sum
   

# SHort notes : 
# - If sorted + pair → try two pointers
# - If constraint monotonic → binary search
# - If rearrangement → greedy