from random import random

a = []
for i in range(0,3000):
    n = int(random()*5000)
    while n in a:
        n = int(random()*5000)
    a.append(n)

def quicksort(a):
    #print(a)
    li = 0
    ls = len(a)
    if(ls > 1):
        r = particion(a,li,ls)
        a[li:r] = quicksort(a[li:r])
        a[r+1:ls] = quicksort(a[r+1:ls])
    return a[li:ls]

def particion(a,li,ls):
    l = li
    for i in range(li,ls-1):
        if a[i+li] < a[ls-1]:
            aux = a[i+li]
            a[i] = a[l]
            a[l] = aux
            l += 1
    aux = a[ls-1]
    a[ls-1] = a[l]
    a[l] = aux
    #print(f"{a=}, {l=}")
    return l
    '''
    '''
