n=input()
c=0
s=""
for i in range(len(n)):
    s=s+n[i]
    if s.count('R')==s.count('L'):
        c+=1
print(c)