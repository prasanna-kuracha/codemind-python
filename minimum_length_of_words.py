n=input()
n=n.split()
k=900
for i in n:
    if len(i)<k:
        k=len(i)
print(k)    