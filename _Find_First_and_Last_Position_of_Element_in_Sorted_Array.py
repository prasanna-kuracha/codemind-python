n=int(input())
a=list(map(int,input().split()))
k=int(input())
if a.count(k)==0:
    print('-1 -1')
else:    
    for i in range(0,len(a)-1):
        if k==a[i]:
           print(i,end=" ")
           break
    for i in range(n-1,-1,-1):
        if k==a[i]:
            print(i,end=" ")
            break    
