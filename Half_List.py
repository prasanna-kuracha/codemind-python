n=int(input())
a=list(map(int,input().split()))
m=n//2 
b=[]
s=[]
for i in range(n-1,m-1,-1):
    if a[i] not in s:
        s.append(a[i])
print(*s,end=" ") 
for i in range(0,m):
    if a[i] not in b:
        b.append(a[i])
print(*b)
    