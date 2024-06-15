a, b = input().split()
A = int(a)
B = int(b)
C = B - 45

if C < 0:
    A = A-1
    B = 60 + B -45
    if A < 0:
        A = 23
else:
    B = B - 45
    if A < 0:
        A = 23

print(A, B)