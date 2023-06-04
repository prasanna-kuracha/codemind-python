n=input()
n=n.split()
n=n[::-1]
b=[]
for i in range(len(n)):
    x=n[i]
    x=x[::-1]
    b.append(x)
print(*b)    