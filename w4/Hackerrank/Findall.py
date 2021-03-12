import re
s=input()
t=re.findall(r'(?<=[QWRTYPSDFGHJKLZXCVBNM qwrtypsdfghjklzxcvbnm])([AEIOUaeiou][AEIOUaeiou]+)[QWRTYPSDFGHJKLZXCVBNM qwrtypsdfghjklzxcvbnm]',s)
if len(t)!=0:
    for i in range(len(t)):
        print(t[i])
else:
    print(-1)  