num=int(input())
a=[]
x=2
while(num!=1):
	if num%x==0:
		num=num//x
		a.append(x)
		x=2
	else:
		x=x+1
ans=''
for x in a:
	ans=ans+" "+str(x)
print(ans)
