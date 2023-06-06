a = input()
b = input()

a = a.split(" ")
b = b.split(" ")

a1 = []
for i in a:
    a1 = a1 + [int(i)]
b1 = []
for i in b:
    b1 = b1+ [int(i)]

s = set()
for i in a1:
    s.add(i)
for i in b1:
    s.add(i)
result= len(s)
print(result)
