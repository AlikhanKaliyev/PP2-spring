import re
n=int(input())
for i in range(n):
    s=input()
    t=re.search(r'[A-Za-z]+\s<[A-Za-z][A-Za-z-._0-9]*@[A-Za-z]+\.[A-Za-z]{1,3}>',s)
    if t:
        print(t.group())