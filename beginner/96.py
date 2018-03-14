p=input()
    c=0
    for i in range(2,p//2):
        if(p%i==0):
            c=1
    if(c==1):
        print("YES")
    else:
        print("NO")
