h, b, c, s = map(int, input().split())
a = (h * b * c * s) / (8 * 1024 * 1024)
print(format(a, ".1f"), "MB")
