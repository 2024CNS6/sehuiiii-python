n = int(input())

a = [["0" for _ in range(19)] for _ in range(19)]

for i in range(n):
    x, y = map(int, input().split())
    a[x-1][y-1] = "1"
    
for k in a:
    print(" ".join(k))