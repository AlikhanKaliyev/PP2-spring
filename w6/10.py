def lol(List):
    l=[]
    for i in List:
        if i%2==0:
            l.append(i)
    return l
k=[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lol(k))