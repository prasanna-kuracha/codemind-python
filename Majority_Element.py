n=int(input())
a=list(map(int,input().split()))
x=0

for i in a:
    s=a.count(i)
    if s>x:
        x=s
        y=i
print(y)
    