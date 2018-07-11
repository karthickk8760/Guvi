n=int(input());
k=int(input());
a=[];
for i in range(0,n):
    x=input();
    a.append(x);
a.sort();
if ((k<=n) and (k>=0)):
    print(a[k+1]);
