a=input();
    b=input();
    c=[]
    f=[]
    e=0;
    for i in range(0,a):
        d=input();
        c.append(d);
    for i in range(0,len(c)):
        if(i%2!=0):
            f.append(c[i-1]);
    print(f[b-1]);
