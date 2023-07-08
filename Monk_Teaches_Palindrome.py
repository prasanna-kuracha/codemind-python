t=int(input())
for i in range(1,t+1):
    n=input()
    if n!=n[::-1]:
        print('NO')
    else:
        if len(n)%2==0:
            print('YES','EVEN')
        else:
            print('YES','ODD')
    
    