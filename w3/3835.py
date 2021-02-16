a=input().split()
r=[]
for i in range(len(a)):
    if int(a[i])>0:
        r.append(int(a[i]))
r.sort()
print(r[0])
