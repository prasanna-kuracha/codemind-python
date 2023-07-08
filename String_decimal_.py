t=int(input())
for i in range(1,t+1):
    n=input()
    k='0123456789'
    for i in range(len(n)):
        if n[i] not in k:
            print('False')
            break
    else:
        print("True")