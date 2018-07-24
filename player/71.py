a=int(input());
b=[];
for i in range(a):
    b.append(int(input()));
b.sort();
for i in range(0,len(b)-1):
    for j in range(i,len(b)):
        if (b[j]>=b[i]) and i!=j:
            print(b[j]);
            break;
