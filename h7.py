a=input()
    b=[]
    c=0
    for i in range(0,a):
        d=input()
        b.append(d)
    for i in range(0,len(b)):
        if(b[i]%2==0 and (i+1)%2==0 or b[i]%2!=0 and (i+1)%2!=0 ):
            print(b[i])
