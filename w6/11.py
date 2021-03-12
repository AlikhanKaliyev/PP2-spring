def lol(n):
    k=0
    for i in range(1,n):
        if n%i==0:
            k+=i
    if k==n:
        print('It is perfect')
    else:
        print('It is not perfect')
n=int(input())
lol(n)