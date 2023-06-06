k = int(input())
w = input()
w = w.split(" ")
l=[]
for i in range(len(w)):
    l= l + [int(w[i])]


def kthmin(k,l):
    min = l[0]

    for i in range(k-1):

        for i in l:
            if i < min :
                min = i
        l.pop(int(l .index(min)))
        min = l[0]
    for i in l:
        if i < min:
            min = i
    return min

print(kthmin(k,l))
