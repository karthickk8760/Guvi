def condition():
	n=int(input())
	k=int(input())
	l=[]
	(s1,s2)=([],[])
	for i in range(n):
		l.append(int(input()))
	if n%2!=0:
		s1=l[:n-1]
		s2=l[n-1:n]
	else:
		s1=l[:n//2]
		s2=l[n//2:n]
	print(s1,s2)
	print(max(min(s1),min(s2)))
condition()
