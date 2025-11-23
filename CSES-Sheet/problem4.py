n = int(intput())
arr = list(map(int,input().split()))

total_moves=0
current_max=arr[0]

for i in range(1,n):
    if arr[i]<current_max:
        total_moves += current_max-arr[i]
    else:
        current_max = arr[i]

print(total_moves)
        