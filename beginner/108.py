a,b,c=input(),input(),input();
    d=[]
    d.append(a);
    for i in range(1,c):
        a=a+b;
        d.append(a);
    print(sum(d));
