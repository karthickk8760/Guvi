a=raw_input()
a.lower()
c=[]
for i in range(0,len(a)):
    if(a[i]!='a' and a[i]!='e' and a[i]!='i' and a[i]!='o' and a[i]!='u' ):
        c.append(a[i])
f="".join(c)
print(f[::-1])
