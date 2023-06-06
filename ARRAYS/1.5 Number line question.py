a = input()

a = a[1:-1]
a = a.split(',')
v = []
for i in range(len(a)):
    v = v + [int(a[i])]
left=[]
right=[]
for i in (v):
    if i>0:
        right.append(i)
        
    elif i<0:
        left.append(i)
        
result = left + right
print (result)