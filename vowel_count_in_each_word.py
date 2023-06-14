n=input()
n=n.split()
for i in range(len(n)):
    k='aeiouAEIOU'
    x=n[i]
    p=0
    for i in range(len(x)):
        if x[i] in k:
            p+=1
    print(p,end=" ")