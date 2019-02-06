ef bin(n):
	s=''
	while(n!=0):
		s+=str(n%2)
		n=n//2
	return(s[::-1])
def main():
	n=int(input())
	(out,l)=('',[])
	for i in range(2**n):
		st=bin(i)
		for j in range(n-len(st)):
			out+='0'
		out+=st
		print(out)
		out=''
main()
