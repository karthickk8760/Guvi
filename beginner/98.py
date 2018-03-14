p=input()
    c=[]
    for i in range(0,p):
        d=input()
        c.append(d)
    for i in range(1,len(c)):
        if(i!=c[i-1]):
            print(c[i-1])
