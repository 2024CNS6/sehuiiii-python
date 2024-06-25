n = int(input())
ans = 0
for _ in range(n):
    arr = input()
    for j in range(len(arr)):
        if j != len(arr) - 1:
            if arr[j] == arr[j + 1]:
                continue
            elif arr[j] in arr[j + 1:]:
                break
        else:
            ans += 1
print(ans)