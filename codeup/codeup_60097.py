a, b = map(int, input().split())
X = [["0" for _ in range(b)] for _ in range(a)]

for _ in range(int(input())):
    l, d, x, y = map(int, input().split())
    if d == 0:
        for i in range(y-1, y+l-1):
            X[x-1][i] = "1"
    else:
        for i in range(x-1, x+l-1):
            X[i][y-1] = "1"

for k in X:
    print(" ".join(k))