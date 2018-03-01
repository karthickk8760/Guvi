a=input()
    b=[]
    c=0
    for i in range(0,a):
        d=input()
        b.append(d)
    for i in range(0,len(b)):
        for j in range(i+1,len(b)):
            if(b[i]==b[j]):
                print(b[i])
                c=c+1
        if(c==1):
            break

