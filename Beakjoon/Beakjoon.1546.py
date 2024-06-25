N = int(input())
a = list(map(int, input().split()))
n = max(a)

for i in range(N):
    a[i] = a[i]/n*100

print(sum(a)/N)