def lol(n):
    if n==0:
        return 1
    else:
        k=1
        for i in range(n):
            k=k*(i+1)
        return k
n=int(input())
print(lol(n))