a=input().split()
b=input().split()
e=set()
u=set()
for i in  a:
    e.add(int(i))
for i in  b:
    u.add(int(i))
r=e & u
r=list(r)
r.sort()
print(*r)
