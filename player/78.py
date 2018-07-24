a=int(input());
c=int(input());
b=[];
for i in range(0,a):
    b.append(input());
for i in range(0,c):
    b.append(input());
b.sort();
d=" ".join(b);
print(d)
