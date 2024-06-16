n,m = map(int, input().split())

a = [0]*n

for l in range(m):
  i,j,k = map(int,input().split())
  for x in range(i,j+1):
    a[x-1] = k

for x in range(n):
  print(a[x], end=" ")