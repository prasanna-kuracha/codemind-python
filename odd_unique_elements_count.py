n=int(input())
a=list(map(int,input().split()))
s=0
b=[]
for i in a:
    if i%2!=0:
      if i not in b:
          b.append(i)
print(len(b))          