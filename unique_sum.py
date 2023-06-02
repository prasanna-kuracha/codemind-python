n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
        if i not in b:
            b.append(i)
s=0            
for i in range(len(b)):
    s=s+b[i]
print(s)    
    