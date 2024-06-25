n, m = map(int, input().split())
box = [i for i in range(1, n+1)]
sum = 0
for j in range(m):
    x, y = map(int, input().split())
    sum = box[x-1:y]
    sum.reverse()
    box[x-1:y] = sum

for j in range(n):
    print(box[j], end=" ")