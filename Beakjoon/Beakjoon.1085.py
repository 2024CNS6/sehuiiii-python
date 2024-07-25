x, y, w, h = map(int, input().split())
A = min(x, y, w-x, h-y)
print(A)