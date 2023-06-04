n=input()
a='aeiou'
l='AEIOU'
b=[]
c=[]
for i in range(len(n)):
    if n[i] in a:
        if n[i] not in b:
            b.append(n[i])
    elif n[i] in l:
        if n[i] not in c:
            c.append(n[i])  
if len(a)==len(b) or len(l)==len(c):
    print(True)
else:
    print(False)
