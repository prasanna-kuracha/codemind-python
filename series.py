n=int(input())
k=1
k1=0
d=0
for i in range(1,n+2):
    if i%2==0:
        a=(3**k)-1
        k=k+1
        print(a,end=" ")
    else:
        b=(2**k1)
        d=d+b
        k1=k1+1
        print(d,end=" ")
        