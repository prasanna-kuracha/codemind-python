n=int(input())
a=list(map(int,input().split()))
s=0
x=0
for i in range(n-1,-1,-1):
    s=s+(2**x)*a[i]
    x=x+1
print(s)
