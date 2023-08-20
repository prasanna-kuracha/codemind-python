n=input()
n=n.split(' ')
n=n[len(n)-1]
k=[]
for i in range(len(n)):
    k.append(ord(n[i]))
s=min(k)
h=chr(s)
if h.lower() in n:
    print(h.lower())
else:
    print(h)
