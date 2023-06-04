n=input()
b=[]
for i in n:
    d=int(i)
    if d%2!=0:
        b.append(d*d)
    else:
        continue
for i in b:
    print(i,end="")