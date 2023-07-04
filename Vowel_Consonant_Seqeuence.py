n=input()
k='aeiou'
s=""
for i in n:
    if i in k:
        s=s+'V'
    else:
        s=s+'C'
p=s[0]
q=s[0]
for i in range(1,len(s)):
    if p!=s[i]:
        p=s[i]
        q=q+s[i]
print(q)
    