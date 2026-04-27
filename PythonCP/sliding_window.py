# A sliding window is just 
# Maintain a contiguous subarray[l,r] that satisfies a condition , while moving efficentely

# Two pointers mechanisms
# Expand r+=1
# Shrink l-=1

# Key contraints:
#     You never move pointers backward -> gurantees O(n)

#Pattern 1 : Fixed Size Window
def fixed_window(arr,k):
    n = len(arr)
    
    window_sum = sum(arr[:k])
    best = window_sum
    
    for r in range(k,n):
        window_sum += arr[r]
        window_sum -= arr[r-k]
        best = max(best, window_sum)
        
    return best

#Pattern 2 : Variable window
# Longest Substring with condition
# Smallest subarray >= target

def variable_window(arr):
    n = len(arr)
    l = 0
    ans = 0
    
    for r in range(n):
        #expand
        #update state
        
        while condition_invalid:
            #shrink
            l+=1
        
        ans = max(ans, r-l+1)
    
    return ans

#Pattern 3 : At most k distinct 

from collections import defaultdict

def at_most_k(arr,k):
    count = defaultdict(int)
    l = 0
    res = 0
    
    for r in range(len(arr)):
        count[arr[r]]+=1
        
        while len(count)>k:
            count[arr[l]]-=1
            
            if count[arr[l]] == 0:
                del count[arr[l]]
            i+=1
        res += (r-l+1)
        
    return res

# Pattern:4 Longest Valid Window
# EX: Longest substring without repeating characters

def longest_unique(s):
    seen = set()
    l=0
    best=0
    
    for r in range(len(s)):
        while s[r] in seen:
            seen.remove(s[l])
            l+=1
        
        seen.add(s[r])
        best = max(best, r-l+1)
        
    return best

#Pattern 5 :Frequency Constraints
# Ex: Replace at mos k chars
# Max repeating char window

def longest_repeating(s,k):
    from collections import defaultdict
    
    count = defaultdict(int)
    l=0
    maxf = 0
    res = 0
    
    for r in range(len(s)):
        count[s[r]] +=1
        maxf = max(maxf,count[s[r]])
        
        while (r-l+1)-maxf >k:
            count[s[l]] -=1
            l+=1
        
        res=max(res, r-l+1)
    
    return res

#Performance :
import sys
input = sys.stdin.readline

def solve():
    n,k = map(int, input().split())
    arr = list(map(int,input().split()))
    
    l = 0
    res = 0
    
    curr = 0
    
    for r in range(n):
        curr += arr[r]
        
        while curr>k:
            curr -= arr[l]
     
# Micro-Optimisation:
#     Prefer
#     list over dict if the range is small
#     array or prellocated lists
#     Avoid Counter(slow)
#     Avoid repeated len(dict) if possible
    
# Replace dict with list

count = [0]*26

# Avoid functions call inside loop

# Pattern Recoginstion CheatSheet

# Problem Statement -> Pattern

# Subarray with sum <=k -> Variable window
# excatly k distinct -> atMostTick
# longest substring without repeat -> set + shink
# fixed size k -> rolling window
# min window substring -> shrink aggressively
#min window substring -> skrink aggressively

# Sliding Window + binary search

def check(arr,k,L):
    #Can we find window of size L with sum<=k
    
    curr = sum(arr[:L])
    if curr <=k:
        return True
    
    for i in range(L, len(arr)):
        curr += arr[i] - arr[i-L]
        if curr <=k:
            return True
        
    return False

def solve(arr,k):
    l,r = 0, len(arr)
    ans = 0
    
#Performace Insight
# Complexity : O(n log n)
# Often Pass when:
# Pure sliding windown fails
# constraints ~1e5- 1e6

# If condition is already montonic with window:
#     you don't need binary search(use pure sliding window O(n))

#Sliding Window + Prefix Sum
# This is underated but extremely powerful

# WHen to Use:
#     Trigger:
#         Negative numbers present
#         Sum queries needed fast
#         "excat sum"= k
# Sliding window alone breaks with negative

#Core Idea

# Use prefix sum
# prefix[i] = sum(0->i)
# Then:
#     sum(l,r) = prefix[r] - prefix[l-1]

#Pattern:1

def subarray_sum_k(arr,k):
    from collections import defaultdict
    
    prefix = 0
    count = defaultdict(int)
    count[0] = 1
    
    res = 0
    
    for x in arr:
        prefix +=x
        if prefix - k in count:
            res += count[prefix-k]
        
        count[prefix] +=1
    
    return res

# Why this beats sliding window
# Sliding window works only when
# All element>=0
# Prefix sum works:
# with negative
# with excat sum queries 

# Hybrid Insight(Important)
# Sometimes:
# Use prefix sum + window boundary logic
# "Longest subarray with sum<=k (with negative)"

# Requires advance technique ( ordered map / binary search on prefix)

# Trap:
#     Dont recompute prefix repeatedly
#     use  running prefix variable 

Advanced Sliding Window Tricks
Tricks:1
Instead of solving directly of 
excatly(k) = atMost(k) - atMost(k-1)

def at_most_k(arr,k):
    from collections import defaultdict
    
    count = defaultdict(int)
    l = 0
    res = 0
    
    for r in range(len(arr)):
        count[arr[r]] +=1
        
        while len(count)>k:
            count[arr[l]]-=1
            if count[arr[l]] == 0:
                del count[arr[l]]
            l+=1
            
        res += (r-l+1)
    return res

def excatly_k(arr,k):
    return at_most_k(arr,k)-at_most_k(arr,k-1)
    
    
#Trick2: Contribution Technique
# Instead of finding best window:
# Count how many subarrays each index contributes
# Used in:
#     Counting Problems
#     No max/min

# Trick 3 : Lazy Max Fequency(Critical)
# maxf = max(maxf, count[s[r]])
# Even if maxf becomes stale -> still correct

# why ? 
# window shrik condition remain safe

# Trick 4: Two windows Simultaneously
# Used in tricky CF problems.
# Example:
#     window1 -> <=K
#     window2 -> <=k-1
# then,
# answer += difference in windows

# Trick 5 Sliding Window + Greedy
# Example:
#     Min window substring
#     Always shrink when valid

# for r in range(n):
#     add(r)
    
#     while valid:
#         update_answer()
#         remove(1)
#         l+=1

# Micro-Optimised Version(for CF)
def solve():
    import sys
    input = sys.stdin.readline
    
    n,k = map(int, input().split())
    
    arr = list(map(int, input().split()))
    
    count = {}
    l = 0
    res = 0
    
    for r in range(n):
        count[arr[l]] = count.get(arr[r],0)+1
        
        while len(count)>k:
            count[arr[l]] -=1
            if count[arr[l]] == 0:
                del count[arr[l]]
            l+=1
        
        res += r - l + 1
        
# Final Mental Model:
# ALways ask:
#     Is it contigous? -> Sliding Window
#     Is constraints monotonic?-> Add binary search
#     Are there negative? Prefix Sum
#     Is it counting excatly K? atMost trick

#Instant pattern recognition + picking correct hybrid

# Situation -> Tool
# positive array -> sliding window
# negitive -> prefix
# answer space -> binary search
# excat count -> atMost trick
    
    
        