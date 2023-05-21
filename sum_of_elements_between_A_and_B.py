n=int(input())
s=0
a=list(map(int,input().split()))
p,q=map(int,input().split())
for i in range(len(a)):  #level 19 lo elements blw 
    if(p<=a[i]<=q):
        s=s+a[i]
print(s)        
