a=input()
    b=[]
    for i in range(0,a):
        d=input()
        b.append(d)
    for i in range(0,len(b)):
        for j in range(i+1,len(b)):
            for k in range(j+1,len(b)):
                if(a[i]+a[j]==a[k]):
                    print(a[i]+" "+a[j]+" "+a[k])
