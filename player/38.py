a=input()
b=[]
for i in range(1,a+1):
    if a%i==0:
        if i%2==0:
            i=str(i)
            b.append(i)
c=" ".join(b)
print(c)
