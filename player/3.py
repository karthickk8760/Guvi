a=input()
    c=0
    while(a!=0):
        b=a%10
        c=b+(c*10)
        a=a/10
    print(c)
