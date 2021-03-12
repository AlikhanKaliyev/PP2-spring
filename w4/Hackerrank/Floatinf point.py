import re
n=int(input())
for i in range(n):
    s=input()
    x=re.search(r'^[+-]?\d*\.[0-9]+$',s)
    if x!=None:
        print('True')
    else:
        print('False')