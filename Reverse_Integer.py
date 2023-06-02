n=int(input())
if n>0:
   q=n
   s=0
   while q!=0:
       r=q%10
       s=s*10+r
       q=q//10
   print(s) 
else:
    s=0
    n=(-n)
    while n!=0:
        r=n%10
        s=s*10+r
        n=n//10
    print(-s)    
      
       