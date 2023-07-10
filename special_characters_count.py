n=input()
a=b=c=d=0
for i in range(len(n)):
    x=ord(n[i])
    if n[i]!=' ':
        if x>=65 and x<=90:
            a+=1
        elif x>=97 and x<=122:
            b+=1
        elif x>=48 and x<=57:
            c=c+1
        else:
            d=d+1
print(d)