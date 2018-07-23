s=list(input());
k=int(input());
res=[];
for i in range(k+1,len(s)):
    res.append(s[i]);
for i in range(0,k+1):
    res.append(s[i]);
rot="".join(res);
print(rot);
