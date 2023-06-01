n=int(input())
a=list(map(int,input().split()))
i=n-1
while i!=0:
    if a[i]%2!=0:
        print(a[i])
        break
    i=i-1