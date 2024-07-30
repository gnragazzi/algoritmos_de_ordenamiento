from random import random

a = []
for i in range(0,3000):
    n = int(random()*5000)
    while n in a:
        n = int(random()*5000)
    a.append(n)

def merge(a,m):
    i = 0
    j = m + 1
    n = len(a)
    b = []
    for k in range(0,n):
        if(j >= n):
            b.append(a[i])
            i += 1;
        elif(i>m):
            b.append(a[j])
            j += 1;
        elif(a[i]<a[j]):
            b.append(a[i])
            i += 1;
        else:
            b.append(a[j])
            j += 1;
    return b
        

def mergesort(a):
    li = 0
    ls = len(a)
    if(ls > 1):
        m = int((li + ls - 1)/2)
        a[li:m+1] = mergesort(a[li:m+1])
        a[m+1:ls] = mergesort(a[m+1:ls])
        a = merge(a,m)
    return a
