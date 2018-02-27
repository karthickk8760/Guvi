a=input()
b=[]
c=0
d=0
e=[]
f=0
for f in range(0,a):
    A=input()
    b.append(A)
   
for c in range(0,len(b)):
    for d in range(c+1,len(b)):
        if(b[c]==b[d]):
            e.append(b[c])
e.sort()
print(e)
