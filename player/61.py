n=int(input());
x=int(input());
e=[];
c=0;
for i in range(0,n):
    el=int(input());
    e.append(el);
for i in range(0,n):
    for j in range(i,n):
        if e[i]+e[j]==x:
           c+=1;
if c>0:
    print("Yes");
else:
    print("No");
