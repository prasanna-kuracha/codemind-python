a=list(map(int,input().split()))
b=list(map(int,input().split()))
s=c=0
for i in range(len(a)):
    if a[i]>b[i]:
        c=c+1
    elif a[i]<b[i]:
        s=s+1
    else:
        continue
print(c,s)    