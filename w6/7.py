def lol(s):
    n=0
    l=0
    for i in s:
        if ord('A')<=ord(i)<=ord('Z'):
            n+=1
        if ord('a')<=ord(i)<=ord('z'):
            l+=1
    print('No. of Upper case characters :',n)
    print('No. of Lower case Characters :',l)
lol('The quick Brow Fox')