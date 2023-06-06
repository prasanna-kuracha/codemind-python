n=int(input())
a=list(map(int,input().split()))
e=min(a) #1
s=str(e) # '1'
f=len(s) #1
b=[]
for i in a:
    x=str(i)
    if len(x)==f:
        b.append(x)
print(len(b))       