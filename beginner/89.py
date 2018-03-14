a=raw_input()
b=[]
for i in range(0,len(a)):
    b.append(a[i])
b.sort()
c="".join(b)
print(c)
