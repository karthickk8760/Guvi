 def main():
	n=int(input())
	m=int(input())
	l=[]
	r=[]
	for i in range(n):
		for j in range(m):
			l.append(int(input()))
		r.append(l)
		l=[]
	for i in r:
		i.sort()
	(s,w)=([],[])
	for i in range(m):
		for j in range(n):
			s.append(r[j][i])
		w.append(s)
		s=[]
	r=[]
	for i in w:
		i.sort()
	for i in range(n):
		for j in range(m):
			r.append(w[j][i])
		print(r)
		r=[]
main()
