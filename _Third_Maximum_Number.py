n=int(input())
a=list(map(int,input().split()))
k1=0
k2=0
k3=0
for i in a:
    if i>k1:
        k1=i
for i in a:
    if i<k1 and i>k2:
          k2=i
for i in a:
    if i>k3 and i<k1 and i<k2:
           k3=i
if k3>0:
    print(k3)
else:
    print(k1)