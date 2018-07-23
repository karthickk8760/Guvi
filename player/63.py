n=int(input());
al=[];
bl=[];
aset=set()
for i in range(0,n):
    a=input();
    al.append(a);
for i in range(0,n):
    b=input();
    bl.append(b);
for i in al:
   if i in bl:
       aset.add(i);
res=" ".join(aset);
print(res)
