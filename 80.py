a=input()
b=list(str(a))
c=0
for c in xrange(0,len(b)):
    if(((int(b[c]))%2)!=0):
        print(b[c])
