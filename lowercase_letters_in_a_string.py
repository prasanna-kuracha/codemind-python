a=input()
b=a.lower()
c=0
for i in range(len(a)):
    if a[i]==b[i] and a[i]!=' ':
        c+=1
print(c)        