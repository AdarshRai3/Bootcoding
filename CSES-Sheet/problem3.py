s=input().strip()

max_len=1
curr_len=1

for i in range(1,len(s)):
    if s[i]==s[i-1]:
        curr_len+=1
        
    else:
        max_len=max(max_len, curr_len)
        curr_len=1

print(max(curr_len, max_len))