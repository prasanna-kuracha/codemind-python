n=input()
n=n.split()
k=0
for i in n:
    if len(i)>k:
        k=len(i)
print(k)    