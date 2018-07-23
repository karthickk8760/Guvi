s=list(input());
s1=list(input());
c=0;
for i in s:
    if i in s1:
        c+=1;
if c>0:
    print("yes");
else:
    print("No");
