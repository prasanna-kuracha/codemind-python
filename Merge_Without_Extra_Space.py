n=int(input())
for i in range(1,n+1):
    x,y=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=[]
    for i in a:
        if i not in c:
            c.append(i)
    for i in b:
        if i not in c:
            c.append(i) 
    k=sorted(c)        
    print(*k)        
            
    