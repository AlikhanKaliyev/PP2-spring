def lol(a,b,c):
    l=[]
    l.append(a)
    l.append(b)
    l.append(c)
    l.sort()
    return l[2]

a=int(input())
b=int(input())
c=int(input())
print(lol(a,b,c))
