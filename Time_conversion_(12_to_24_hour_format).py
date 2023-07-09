n=input()
n=n.split(":")
hh=int(n[0])
x=n[1].split(" ")
mm=int(x[0])
t=x[1]
if t=='PM':
    if hh>0 and hh<12:
        k=hh+12
        print(str(k)+':'+x[0])
if t=='AM':
    if hh>0 and hh<12:
        print(n[0]+':'+x[0])
if hh==12:
    if t=="PM":
        print('12:00')
    else:
        print("00:00")