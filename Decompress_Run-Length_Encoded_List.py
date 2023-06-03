n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(0,n,2):
    k=a[i]
    h=a[i+1]
    for j in range(1,k+1):
        b.append(h)
print(*b)        
        
        