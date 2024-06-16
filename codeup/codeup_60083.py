
r, g, b = map(int, input().split())

colors = []

for i in range(r):
    for j in range(g):
        for k in range(b):
            colors.append((i, j, k))

for color in colors:
    print(*color)

print(len(colors))
