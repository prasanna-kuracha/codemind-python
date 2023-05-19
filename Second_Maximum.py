n=int(input())
for i in range(1,n+1):
    arr = map(int, input().split())
    b=list(arr)
    b.sort()
    print(b[-2])