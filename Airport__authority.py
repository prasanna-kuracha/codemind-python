n=int(input())
b=[]
for i in range(n):
    b.append(int(input()))
t=int(input())
c=0
for j in range(n):
    if b[j]<=t:
        c=c+1
    else:
        c=c+2
print(c)
