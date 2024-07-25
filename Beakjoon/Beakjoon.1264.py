a = ['a', 'i', 'e', 'o','u', 'A', 'I', 'E', 'O', 'U']

while True:
    count = 0
    S = input()
    if S == '#':
        break
    for s in S:
        if s in a:
            count += 1
    print(count)
