m=int(input())
a=list(set(map(int,input().split())))
k=int(input())
a.sort()
f=a[len(a)-k]
print(f)