n=input()
for i in n:
    f=n.count(i)
    if f==1:
        print(n.index(i))
        break
else:
    print('-1')