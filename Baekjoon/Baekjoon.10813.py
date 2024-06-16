n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(i + 1) # 리스트 초기화 1~n 까지의 정수를 가짐

for i in range(m):
    a, b = map(int, input().split())
    arr[a - 1], arr[b - 1] = arr[b - 1], arr[a - 1]

for i in range(n):
    print(arr[i])
