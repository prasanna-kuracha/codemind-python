n=int(input())
k=n*n
c=0
while n!=0:
    r=n%10
    m=k%10
    if r!=m:
        c=1
        break
    n=n//10
    k=k//10
if c==1:
    print('Not an Automorphic Number')
else:
    print('Automorphic Number')