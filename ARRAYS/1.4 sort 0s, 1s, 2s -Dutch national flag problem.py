a = input()
a = a[1: -1]
a = a.split(' ')
v= []
for i in range(len(a)):
    v = v+ [int(a[i])]

k = []
while (len(v)>0):
    min = v[0]
    for i in range(len(v)):
        if (v[i]<=min):
            min = v[i]
    k.append(min)
    v.remove(min)

result = ' '.join(str(x) for x in k)
print (result)