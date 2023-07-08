t=int(input())
for i in range(1,t+1):
    k=int(input())
    n=input()
    for i in range(len(n)):
        if(n.count(n[i])==1):
            c=1
            print(n[i])
            break
    else:
        print("-1")