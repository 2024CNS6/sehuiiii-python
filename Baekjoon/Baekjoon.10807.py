n = int(input())
a = list(map(int, input().split()))
f = int(input())

cnt = 0
for i in range(n):
    if a[i] == f:
        cnt += 1

print(cnt)