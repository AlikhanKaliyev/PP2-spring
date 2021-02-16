a=input().split()
k=int(input())
if k>=0:
    a=a[k-1:]+a[:k-1]
else:
    k=abs(k)
    a=a[k:]+a[:k]
b=list(a)
print(*b)
