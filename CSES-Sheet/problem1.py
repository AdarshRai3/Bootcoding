import sys 

data = sys.stdin.readline()
write = sys.stdout.write

n = int(data)

while True:
    write(str(n))
    if n == 1:
        break
    write(" ")
    if n&1 == 0:
      n>>=1
    else:
      n=3*n+1