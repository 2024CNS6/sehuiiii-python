d, h, w = map(int, input().split()) 
r = d/(h**2 + w**2)**0.5
print(int(h*r), int(w*r))

## 이 코드가 어려웠던 이유: 수학적인 계산 부분이 어려웠고 특히 계산하는 공삭이 좀 복잡했다.