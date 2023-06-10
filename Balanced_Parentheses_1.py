n=input()
a=b=c=d=e=f=0
for i in range(len(n)):
    if  n[i]=="(":
        a=a+1
    elif n[i]==")":
        b=b+1
    elif n[i]=="{":
        c=c+1
    elif n[i]=="}":
        d=d+1 
    elif n[i]=="[":
        e=e+1 
    elif n[i]=="]":
        f=f+1
if (a==b) and (c==d) and (e==f):
    print(True)
else:
    print(False)
        