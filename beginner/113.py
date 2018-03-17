a=input();
    b=input();
    c=[]
    e=0;
    for i in range(0,a):
        d=input();
        c.append(d);
    for i in range(0,len(c)):
        if(c[i]==b):
            e=e+1;
    print(e);
