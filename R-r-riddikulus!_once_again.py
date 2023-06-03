n,d=map(int,input().split())
a=list(map(int,input().split()))
b=[]
for i in range(d,n):
        b.append(a[i])
for i in range(0,d):
       b.append(a[i])        
print(*b)        
    