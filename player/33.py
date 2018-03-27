a=input()
b=[]
d=0
for i in range(0,a):
    c=raw_input().split()
    b.append(c)
    for i in c:
        if i=='1':
            d=d+1
print(d)    
