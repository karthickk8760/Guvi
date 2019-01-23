def coin(n,l,t):
	k=1
	c=0
	s=0
	l.sort(reverse=True)
	for i in range(n):
		while(s<t):
			s=s+l[i]
			c=c+1
	print(c)

def main():
	n=int(input())
	t=int(input())
	l=[]
	for i in range(n):
		l.append(int(input()))
	coin(n,l,t)
main()
