a=list(raw_input())
    b=list(raw_input())
    c=len(a)
    d=0
    i=0
    j=0
    while c>0:
        d=d+(ord(b[j])-ord(a[i]))
        i=i+1
        j=j+1
        c=c-1
    print(d)
