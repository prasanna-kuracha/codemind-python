
n=int(input())
m=int(input())

def fun(n,m):
    s=0
    for i in range(1,(n//2)+1):
       if n%i==0:
            s=s+i
    p=0        
    for j in range(1,(m//2)+1):
       if m%j==0:
            p=p+j
            
    if n==p and m==s:
        print("Amicable")
    else:
        print("Not Amicable")


fun(n,m)