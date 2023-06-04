n=input()
k=input()
for i in range(len(n)):
    if n[i]==k:
        print(True)
        print(i)
        break
else:
    print('False')