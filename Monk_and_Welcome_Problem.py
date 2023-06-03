n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(len(a)):
    k=a[i]+b[i]
    print(k,end=" ")    