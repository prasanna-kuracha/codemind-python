n=int(input())
a=list(map(int,input().split()))
b=[]
s=[]
for i in a:
    if i not in b:
         b.append(i)
         x=a.count(i)
         s.append(x)
k=len(b)
for i in range(0,k):
    print(b[i],s[i],end=" ")
   