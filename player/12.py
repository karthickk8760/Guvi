def rotate(n,k,l):
	r=[]
	for i in range(n-k,n):
		r.append(l[i])
	for i in range(n-k):
		r.append(l[i])
	print(r)
def main():
		n=int(input())
		k=int(input())
		l=[]
		for i in range(n):
			l.append(input())
		rotate(n,k,l)
main()
