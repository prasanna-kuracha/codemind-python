n=int(input())
s=m=0
a=list(map(int,input().split()))
p,q=map(int,input().split())
for i in range(len(a)):
    if(a[i]<p):
        s=s+a[i]
for i in range(len(a)):
    if(a[i]>q):
        m=m+a[i] 
print(s+m)        
        