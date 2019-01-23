def triplet(tot,l):
	n=len(l)
	for i in range(n-2):
		for j in range(i+1,n-1):
			for k in range(j+1,n):
				if l[i]+l[j]+l[k]==tot:
					return l[i],l[j],l[k]

	return 'none'
  
def main():
	n=int(input())
	l=[]
	for i in range(n):
		l.append(int(input()))
	tot=int(input())
	print(triplet(tot,l))
main()
