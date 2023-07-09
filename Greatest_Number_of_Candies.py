n=int(input())
a=list(map(int,input().split()))
k=int(input())
s=max(a)
for i in a:
    if k+i>=s:
        print(True,end=" ")
    else:
        print(False,end=" ")