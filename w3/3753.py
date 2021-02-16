def lol(some_set):
    print(len(some_set))
    print(*sorted(list(some_set)))




y=input().split()
a=int(y[0])
b=int(y[1])
a1=set()
b1=set()
for i in range(a):
    x=int(input())
    a1.add(x)
for i in range(b):
    x=int(input())
    b1.add(x)
lol(a1 & b1)
lol(a1 - b1)
lol(b1 - a1)


    
