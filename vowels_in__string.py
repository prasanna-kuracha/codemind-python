n=input()
x='AEIOUaeiou'
b=[]
for i in n:
    if i in x:
        if i not in b:
            b.append(i)
print(*b)