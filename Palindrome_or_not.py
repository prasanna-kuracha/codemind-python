n=input()
n=n.lower()
k=n[::-1]
for i in range(len(n)):
    if n[i]!=k[i]:
        print(False)
        break
else:
    print(True)
