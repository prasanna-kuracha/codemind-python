n=input()
n=n.split()
b=[]
for i in range(len(n)):
    if i%2==0:
        s=n[i]
        s=s[::-1]
        b.append(s)
    else:
        b.append(n[i])
print(*b)        
        