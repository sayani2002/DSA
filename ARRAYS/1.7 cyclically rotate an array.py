a = input()
a = a.split(",")

a1 = []
for i in a:
    a1 = a1 + [int(i)]

b= []
b = [a1[-1]] + a1[:(len(a1)-1)]
print (b)