n=int(input());
no=list(input());
if n==len(no):
    for i in no:
        if i=='0':
            print(" ",end=" ");
        else:
            print(i,end=" ");
