n=int(input())
for i in range(1,n+1):
    n=input()
    c=0
    for i in n:
        if i.isdigit():
            print('Yes')
            break
    else:
        print("No")
        