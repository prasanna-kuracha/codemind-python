n=input()
c=0
for i in n:
    if ord(i)>=65 and ord(i)<=90:
        c=c+1
if n[0] in 'abcdefghijklmnopqrstuvwxyz':
    c=c+1
print(c)