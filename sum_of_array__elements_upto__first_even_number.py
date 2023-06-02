n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if i not in b:
        if i%2!=0:
            b.append(i)
        else:
            break
print(sum(b))        