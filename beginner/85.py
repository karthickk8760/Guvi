a=raw_input()
b=[]
c=[]
d=""
e=""
for i in range(0,len(a)):
    if(i%2!=0):
        b.append(a[i])
    else:
        c.append(a[i])
for i in c:
   d=i+d
d=d[::-1]
print(d)
for i in b:
    e=i+e
e=e[::-1]
print(e)
