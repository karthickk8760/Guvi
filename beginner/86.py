a=raw_input()
c=0
for i in range(0,len(a)):
   for j in range(i+1,len(a)):
        if(a[i]==a[j]):
           c=c+1;
if(c>0):
    print("Yes")
else:
    print("No")
