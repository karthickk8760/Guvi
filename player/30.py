st1=raw_input()
st2=raw_input()
k=int(input())
c1=0
c2=0
for x in st1:
	if x not in st2:
		c1=c1+1
for x in st2:
	if x not in st1:
		c2=c2+1
if(c1==c2==k):
	print("Yes")
else:
	print("No")
