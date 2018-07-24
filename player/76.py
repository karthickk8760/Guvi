a=int(input());
b=[];
ce=0;
co=0;
for i in range(a):
    b.append(input());
for i in b:
    if int(i)%2==0:
        ce+=1;
    elif int(i)%2!=0:
        co+=1;
if (ce>co):
    for i in b:
        if int(i)%2!=0:
            print(i);
elif (ce<co):
    for i in b:
        if int(i)%2==0:
            print(i);
