n=int(input())
for i in range(1,n+1):
    a=int(input())
    b=[]
    while a!=0:
        r=a%10
        b.append(r)
        a=a//10
    b.sort()
    for i in range(0,len(b)-1):
       if b[i+1]-b[i]!=1:
          print("NO")
          break
    else:
       print("YES")

    