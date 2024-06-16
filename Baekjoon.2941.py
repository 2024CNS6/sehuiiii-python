a = input()
a1 = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in a1:
    a = a.replace(i, "*")

print(len(a))