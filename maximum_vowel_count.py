n=(input())
n=n.split()
m=0
for i in range(len(n)):
    a='aeiouAEIOU'
    x=n[i]
    p=0
    for i in range(len(x)):
        if x[i] in a:
            p+=1
    if p>m:
        m=p
print(m,end=" ")