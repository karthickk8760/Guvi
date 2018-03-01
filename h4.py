 a=input()
    b=[]
    c=0
    for i in range(0,a):
        d=input()
        b.append(d)
    for i in range(0,len(b)):
        for j in range(0,len(b)):
            if(b[i]==b[j]):
                c=c+1
        if(c==1):
            print(b[i])
        c=0
