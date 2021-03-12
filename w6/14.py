def lol(n):
    n=n.split()
    k=1
    for i in n:
        if len(i)!=len(set(i)):
            k=0
    if k==1:
        print('YES')
    else:
        print('NO')
n=input()
lol(n)
