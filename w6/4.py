def lol(s):
    l=''
    for i in range(len(s)-1,-1,-1):
        l=l+s[i]
    return l
print(lol('1234abcd'))