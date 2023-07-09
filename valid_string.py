n=input()
s=set(n)
b=[]
c=0
for i in s:
    b.append(n.count(i))
for i in b:
    if i!=max(b):
        c=c+1
if c<=1:
    print('Valid String')
else:
    print('Not Valid')