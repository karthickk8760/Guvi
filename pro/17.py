 def main():
	n=int(input())
	l=[]
	f=0
	for i in range(n):
		l.append(int(input()))
	k=int(input())
	for i in range(n-1):
		if l[i]==l[i+1]:
			s=l[i]+l[i+1]
			if s==k:
				f=1
				print('yes')
	if f!=1:
		print('no')
    
main()
