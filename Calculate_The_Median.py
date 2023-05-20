import statistics
n=int(input())
arr=map(int,input().split())
k=list(arr)
k.sort()
c=(n//2)
print(k[c])


