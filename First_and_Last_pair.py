n=int(input())
a=list(map(int,input().split()))
k=n//2+1
i=0
j=n-1
b=[]
while i<=k and j>=k:
        b.append(a[i])
        i=i+1
        b.append(a[j])
        j=j-1
if n%2!=0:
    b.append(a[i])
    print(*b,'0')
else:
    b.append(a[i])
    b.append(a[j])
    print(*b)    
    
        