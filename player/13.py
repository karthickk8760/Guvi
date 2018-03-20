a=input()
b=0
while(a!=0):
    c=a%10
    b=c**2+b
    a=a/10
print(b)
