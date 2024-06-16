n = int(input())
N = list(map(int, input().split()))

value = N[0]

for i in N:
    if i < value:
        value = i
print(value)