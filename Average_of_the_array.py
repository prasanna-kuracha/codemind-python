n=int(input())
arr=list(map(int,input().split()))
for i in range(0,n):
    s=sum(arr)/len(arr)
print(format(s, '.2f'))    
    