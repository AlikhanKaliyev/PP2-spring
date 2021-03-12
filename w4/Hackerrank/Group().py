import re
s=input()
t=re.search(r'([A-Za-z0-9])\1+',s)
if t:
    print(t.group(1))
else:
    print(-1)
