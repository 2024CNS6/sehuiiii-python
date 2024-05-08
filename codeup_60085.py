w, h, b = map(int, input().split())
a = (w * h * b) / (8 * 1024 * 1024)
print(format(a, ".2f"), "MB")