while True:
    num = input("100 보다 작은 수를 입력해주세요 : ")
    num = int(num)
    
    if 1 <= num <= 99:
        break
    else:
        print("잘못된 입력입니다.")

tens = num // 10
ones = num % 10

print(f" 십의 자리: {tens}, 일의 자리: {ones} ")

prime_tens = tens > 1
for i in range(2, int(tens**0.5) + 1):
    if tens % i == 0:
        prime_tens = False
        break

prime_ones = ones > 1
for i in range(2, int(ones**0.5) + 1):
    if ones % i == 0:
        prime_ones = False
        break

if prime_tens and prime_ones:
    print("오늘은 행운이 가득해요!!!")
elif prime_tens or prime_ones:
    print("오늘의 운세는 보통입니다~ 화이팅!")
else:
    print("오늘의 운세는 꽝...ㅠ 그래도 킵고잉~")

## 코드가 처음부터 끝까지 어떻게 실행되는지 이해하기 어려웠고, 특히 반복문과 조건문이 함께 사용되는 부분은 복잡하게 느껴졌습니다.