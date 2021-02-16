a=int(input())
d={}
for i in range(a):
    first,second=[t for t in input().split()]
    d[first]=second
    d[second]=first
k=input()
print(d[k])
