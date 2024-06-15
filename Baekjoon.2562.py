cnt = 1
max = -1
for i in range(9):
    a = int(input())
    if max < a:
        max = a
        maxi = cnt
    cnt = cnt+1

print(max)
print(maxi)

# 다른 풀이
# a = []
# for i in range(9):
#     a.append(int(input()))

# print(max(a))
# print(a.index(max(a))+1)