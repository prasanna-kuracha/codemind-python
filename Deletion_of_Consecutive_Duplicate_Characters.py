k=int(input())
for i in range(1,k+1):
    n=input()
    b=[]
    c=0
    for i in range(len(n)):
        if len(b)==0:
            b.append(n[i])
        elif n[i]!=b[len(b)-1]:
            b.append(n[i])
        else:
            c=c+1
    print(c)
    
        