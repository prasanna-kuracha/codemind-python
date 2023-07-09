n=input()
n=n.split(":")
hh=int(n[0])
mm=int(n[1])
if hh>12 and hh<24:
    k=hh-12
    if k<=9:
        print("0"+str(k)+':'+n[1]+" "+'PM')
    else:
        print(str(k)+':'+n[1]+' '+'PM')
if hh>0 and hh<12:
    print(n[0]+":"+n[1]+' '+'AM')
if hh==00:
    print('12:00 AM')
if hh==12:
    print("12:00 PM")