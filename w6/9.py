def lol(n):
    if n<=1:
        return False
    k=0
    for i in range(2,n+1):
        if n%i==0:
            k+=1
    if k==1:
        return True
    else:
        return False
n=int(input())
print(lol(n))
