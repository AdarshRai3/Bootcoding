import sys
data = sys.stdin.read().strip().split()

n = int(data[0])

xor = 0
idx = 1

# XOR with numbers 1..n
for i in range(1, n + 1):
    xor ^= i

# XOR with given n-1 numbers
for i in range(n - 1):
    xor ^= int(data[idx])
    idx += 1

print(xor)
