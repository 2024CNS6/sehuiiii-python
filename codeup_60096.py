a = []
for _ in range(19):
    arr = input().split()
    a.append(arr)

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    for k in range(19):
        a[k][y-1] = str(int(not int(a[k][y-1])))
        a[x-1][k] = str(int(not int(a[x-1][k])))
        
for k in a:
    print(" ".join(k))
