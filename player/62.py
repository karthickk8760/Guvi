n=int(input());
a=[];
for i in range(1,n):
    c=n/i;
    if (n%i==0) and (c%2!=0):
        a.append(i);
print(min(a));
