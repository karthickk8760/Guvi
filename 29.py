a=input()
    b=a//60
    c=a%60
    if(a<60):
        print("0 "+str(a))
    else:
        print(str(b)+" "+str(c))
