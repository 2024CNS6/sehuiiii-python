a = input()
alphabet = {chr(i + 96): i for i in range(1, 27)}

b = a.split()
print(len(b))

c = sum(alphabet[i[0]] for i in b)
print(c)

## 이 코드가 어려웠던 이유:  sum() 함수가 어떻게 작동하는지 이해하지 못했고 딕셔너리의 데이터 구조를 활용하는 것이 쉽지 않았다.