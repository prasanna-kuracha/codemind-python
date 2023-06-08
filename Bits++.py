n=int(input())
c=0
for i in range(1,n+1):
    a=input()
    if '++' in a:
        c=c+1
    if '--' in a:
        c=c-1
print(c)        