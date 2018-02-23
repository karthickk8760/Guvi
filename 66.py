a=input()
c=0
f=0
e=a/2
for c in range(2,e):
    if((a%c)==0):
        f=f+1
if(f==0):
    print("prime number")
else:
    print("Not prime number")
