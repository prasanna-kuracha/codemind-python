n=input()
x='aeiou'
b=[]
for i in range(len(n)):
    if n[i] in x:
        if n[i] not in b:
            b.append(n[i])
if len(x)==len(b):
    print('0')
else:
    for i in x:
        if i not in b:
            print(i,end=" ")
        