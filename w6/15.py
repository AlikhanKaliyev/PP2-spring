def lol(n):
    l=[]
    p=''
    for i in range(len(n)):
        if i==len(n)-1:
            if n[i]!='-':
                p=p+n[i]
                l.append(p)
            else:
                l.append(p)
        if n[i]!='-':
            p=p+n[i]
        if n[i]=='-':
            l.append(p)
            p=''
    l.sort()
    for i in range(len(l)):
        print(l[i]+'-', end='')
n=input()
lol(n)
