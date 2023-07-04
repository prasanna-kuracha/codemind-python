n=input()
k=int(input())
c=n.count('a')*(k//len(n))
s=n[:k%len(n)]
l=s.count('a')
print(c+l)
