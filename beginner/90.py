a=raw_input()
b=[]
for i in range(0,len(a)):
   if(a[i].isdigit()):
       b.append(a[i])
c="".join(b)
print(c)
