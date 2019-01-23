string=input()
strlist=list(string)
op=[]
for i in range(len(strlist)):
    if i%2==0:
        if (i+1)<len(strlist):
            op.append(strlist[i+1])
        op.append(strlist[i])
print("".join(op))
