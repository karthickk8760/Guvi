def fun():
	N=int(input())
	W=int(input())
	(we,v)=([],[])
	for i in range(N):
		we.append(int(input()))
	for i in range(N):
		v.append(int(input()))
	sum=0
	i=0
	c=0
	for i in range(N):
		sum+=we[i]
		if sum>W:
			break
		c+=v[i]
	print(c)
fun()
