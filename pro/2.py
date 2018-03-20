a,b=raw_input(),input()
    e=1
    a=list(a)
    while(e!=0):
        e=e-1
        del(a[e])
    print("".join(a))
