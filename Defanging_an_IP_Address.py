n=input()
b=[]
for i in n:
    if i=='.':
        b.append('[.]')
    else:
        b.append(i)
for i in b:
    print(i,end="")
        