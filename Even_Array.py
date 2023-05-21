n=int(input())
arr=list(map(int,input().split()))
for i in range(0,n):
    if arr[i]%2==0:
        s=1
    else:
        s=0
        break
if s==1:
    print(True)
else:
    print(False)
