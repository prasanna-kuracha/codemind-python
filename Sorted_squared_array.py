n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    k=i*i
    b.append(k)
b.sort()
print(*b)
    