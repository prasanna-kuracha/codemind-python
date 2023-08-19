n=int(input())
a=list(map(int,input().split()))
if a[n-3]+a[n-2]!=a[n-1]:
    print('no')
else:
    for i in range(0,n-2):
       if a[i]+a[i+1]!=a[i+2]:
          print('no')
          break
    else:
        print('yes')