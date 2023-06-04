n=input()
n=n.split()
b=[]
for i in range(len(n)):
    y=n[i]
    y=y[::-1]
    b.append(y)
print(*b)    