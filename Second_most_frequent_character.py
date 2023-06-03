n=input()
m1=0
for i in n:
    if n.count(i)>m1:
        m1=n.count(i)
        p1=i
m2=0
p2=-1
for i in n:
    if n.count(i)>m2 and n.count(i)<m1:
        m2=n.count(i)
        p2=i
print(p2)        