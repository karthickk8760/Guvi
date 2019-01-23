def hcf(n1,n2):
	while(n2!=0):
		t=n2
		n2=n1%n2
		n1=t
	return n1
def main():
	n=int(input())
	q=int(input())
	(l,r)=([],[])
	for i in range(n):
		l.append(int(input()))
	print(l)
	for c in range(q):
		n1=int(input())
		n2=int(input())
		r.append(hcf(l[n1-1],l[n2-1]))
	for i in r:
		print(r)
main()
