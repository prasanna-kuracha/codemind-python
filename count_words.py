n=input()
n=n.split()
v='AEIOUaeiou'
c=0
for i in range(len(n)):
    x=n[i]
    if x[0] in v and x[len(x)-1] not in v:
        c=c+1
print(c)        