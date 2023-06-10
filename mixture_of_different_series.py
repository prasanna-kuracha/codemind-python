n=int(input())
for i in range(1,n+2):
    if i%2!=0:
        i=i//2
        k=(2**i)-1
        print(k,end=" ")
    else:
        i=i//2
        s=(3**(i-1))-1
        print(s,end=" ")
        
        