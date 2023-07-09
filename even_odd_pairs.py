n=int(input())
a=list(map(int,input().split()))
s=[]
k=[]
for i in range(len(a)):
    if a[i]%2==0:
        s.append(a[i])
    else:
        k.append(a[i])
f=[]
i=j=0
while i<len(s) and j<len(k):
    f.append(s[i])
    f.append(k[j])
    i=i+1
    j=j+1
while i<len(s):
    f.append(s[i])
    i=i+1
while j<len(k):
    f.append(k[i])
    j=j+1
if len(f)%2!=0:
    f.append('0')
print(*f)
    
    
