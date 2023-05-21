n=int(input())
s=k=0
a=list(map(int,input().split()))
c=int(input())
for i in range(len(a)):
    if(k<c):
        s=s+a[i]
        k=k+1
print(s)        
        
        
    