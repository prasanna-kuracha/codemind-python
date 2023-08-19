n=int(input())
a=list(map(int,input().split()))
si=ei=-1
for i in range(len(a)):
    k=[]
    l=[]
    for j in range(i,len(a)):
        if a[j]==0:
            k.append(a[j])
        else:
            l.append(a[j])
        if len(k)==len(l) and ei-si<j-i:
            si=i
            ei=j
if si!=-1:
    print(si,ei)
else:
    print('-1')
            
        