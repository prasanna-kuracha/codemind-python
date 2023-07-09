n=int(input())
for i in range(n):
    p=2**i
    if p>=n:
        break
    q=p
if abs(n-p)<abs(n-q):
    print(abs(n-p))
else:
    print(abs(n-q))