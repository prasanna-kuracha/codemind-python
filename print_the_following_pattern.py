n=int(input())
f=ord('A')
for i in range(f,f+n,1):
    for j in range(f,f+n,1):
        print(chr(i),end=' ')
    print()  