n=int(input())
s=1
k=n*n
while n!=0:
    r=n%10
    m=k%10
    if r!=m:
        s=0
        break
    n=n//10
    k=k//10
if s==1:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")