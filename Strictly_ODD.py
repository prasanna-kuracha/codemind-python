n=int(input())
a=list(map(int,input().split()))
for i in range(len(a)):
    if i%2==0:
        if a[i]%2==0:
            continue
        else:
            print(False)
            break
else:
    print(True)