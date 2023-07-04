n=input()
k='aeiou'
s=""
for i in range(0,len(n)):
    if len(s)==0:
        if n[i] in k:
            s=s+'V'
        else:
            s=s+'C'
    elif n[i] in k:
        if s[len(s)-1]!='V':
            s=s+'V'
    else:
        if s[len(s)-1]!='C':
            s=s+'C'
print(s)
        