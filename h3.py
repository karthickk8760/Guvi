a=input()
b=[]
c=[]
for i in range(0,a):
    d=input()
    b.append(d)
for i in range(0,len(b)):
    if(i==b[i]):
        c.append(i)
if(len(c)==0):
    print("-1")
else:
    print(c)
