R = int(input())

for i in range(R):
    S, P = input().split()
    for i in range(len(P)):
        print(int(S)*P[i], end='')
    print()