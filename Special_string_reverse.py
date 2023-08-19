n=input()
s=[]
for i in range(len(n)):
    if ord(n[i])>=97 and ord(n[i])<=122:
        s.append(n[i])
p=""
for i in range(len(n)):
    if ord(n[i])>=97 and ord(n[i])<=122:
        p=p+s.pop()
    else:
        p=p+n[i]
print(p)