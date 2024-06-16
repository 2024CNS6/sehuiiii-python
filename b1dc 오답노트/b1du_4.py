n = int(input()) 
a = []
m = 0
for i in range(n):
    a.append(int(input()))

for j in a:
    m += j

if m >= 4700 and m <= 5000:
    print("당신은 인간 저울이군.") 
elif n == 0:
    print("장난해?")
else:
    print("이 감자 네가 다 먹고 다시 가져와.")


## 이 코드가 어려웠던 이유: for 루프가 두 번 사용되었고 특히 반복문을 사용하는 방법과 그것이 어떤 역할을 하는지 이해하기 어려워서 문제를 틀렸던 것 같다.