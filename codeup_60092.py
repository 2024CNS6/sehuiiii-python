n = int(input())
N = list(map(int, input().split()))

answer = [0] * 23

for k in N:
    answer[k-1] += 1
result = " ".join(map(str, answer))
print(result)