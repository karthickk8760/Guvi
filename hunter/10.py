a=int(input());
b=int(input());
c=[];
d=[];
co=0;
for i in  range(a):
    c.append(int(input()));
for i in range(b):
    d.append(int(input()));
c.sort();
d.sort();
for i in d:
    if int(i) in c:
        co+=1;
if co==len(d):
    print("Yes")
else:
    print("No");
    
