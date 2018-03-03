a=raw_input()
    c=0
    for i in range(0,len(a)):
        if(ord(a[i])>=32 and ord(a[i])<=47):
            c=c+1
    print(c)
