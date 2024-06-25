a = [0]*31
for i in range(28):
    n = int(input())
    a[n] = 1

for i in range(1, 31):
    if a[i] == 0:
        print(i, end=" ")