n=int(input())
a=list(map(int,input().split()))
l=[]
x=1
for i in range(len(a)-1,-1,-1):
        r=a[i]+x
        q=r%10
        x=r//10
        l=[q]+l
if x!=0:
    l=[x]+l
for i in l:
    print(i,end=" ")
    
        
    