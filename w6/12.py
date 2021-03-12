def lol(n):
    k=len(n)//2
    if n[:k]==n[:-k-1:-1]:
        print('Yes')
    else:
        print('No')
n=input()
lol(n)