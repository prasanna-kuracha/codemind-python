n=input()
for i in range(len(n)):
    if n.count(n[i])==1:
        print(n[i])
        break
else:
    print('-1')