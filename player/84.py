a=int(input());
b=[];
for i in range(a):
    b.append(int(input()));
b.sort()
dmax=b[1]|b[0];
for i in range(0,len(b)):
    for j in range(i,len(b)):
        if (b[j]|b[i])>dmax:
            dmax=b[j]|b[i];
print(dmax);
