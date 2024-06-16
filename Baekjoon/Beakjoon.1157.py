word = input().upper()
w_l = list(set(word))
a = []

for i in w_l:
    count = word.count(i)
    a.append(count)

if a.count(max(a))>= 2:
    print("?")
else:
    print(w_l[a.index(max(a))])
