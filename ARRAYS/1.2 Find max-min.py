a=input()
def max_min(arr):
    min_val = arr[0]
    max_val= arr[0]
    for num in arr:
        if num <  min_val:
            min_val= num 
        if num > max_val :
            max_val = num 

    return (max_val + min_val)

a = a[1: -1]
a = a.split(',')
v= []
for i in range(len(a)):
    v= v+ [int(a[i])]

print(max_min(v))