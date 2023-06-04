n=int(input())
e=0
o=0
while n!=0:
    r=n%10
    if r%2!=0:
        o=o+1
    else:
        e=e+1
    n=n//10
if e>0 and o>0:
    print("Mixed")
elif e>=1:
    print('Even')
else:
    print('Odd')