def xor(l,s,e):
	m=0
	for i in range(s-1,e):
		m=m^l[i]
	return m
def main():
	n=int(input())
	l=[]
	for i in range(n):
		l.append(int(input()))
	q=int(input())
	out=[]
	for i in range(q):
		s=int(input())
		e=int(input())
		out.append(xor(l,s,e))
	for i in out:
		print(i)
 main()
