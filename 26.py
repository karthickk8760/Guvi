a=input()
    b=[]
    for i in range(0,a):
        d=input()
        b.append(d)
    for i in range(0,len(b)):
        for j in range(i+1,len(b)):
            if(b[i]>b[j]):
                t=b[i]
                b[i]=b[j]
                b[j]=t
    if(a%2==0):
        print((b[a/2]+b[(a/2)-1])/2)
    else:
        print(b[(a-1)/2])
