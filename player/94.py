n=input()
flag=0
nli=list(n)
for i in nli:
    if nli.count(i)>1:
        flag+=1
if flag==0:
    print("No")
else:
    print("Yes")
