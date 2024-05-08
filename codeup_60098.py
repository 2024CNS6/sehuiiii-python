X = []
for _ in range(10):
    X.append(input().split())
    
x, y = 1, 1
while x <= 8 and y <= 8:
    if X[x][y] == "2":
        X[x][y] = "9"
        break
    X[x][y] = "9"
    if X[x][y+1] == "1" and X[x+1][y] == "1":
        break
    elif X[x][y+1] == "1":
        x += 1
    else:
        y += 1

for k in X:
    print(" ".join(k))