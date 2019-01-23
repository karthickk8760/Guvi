def main():
	r,c=map(int,input().split())
	ar=[]
	for i in range(r):
		l=list(map(int,input().split()))
		ar.append(l)
	s=[[0 for i in range(c)] for j in range(r)]
	for i in range(1,r):
		for j in range(1,c):
			if ar[i][j]==1:
				s[i][j]=min(s[i][j-1],s[i-1][j],s[i-1][j-1])+1
			else :
				s[i][j]=0
	max_s=s[0][0]
	max_i=0
	max_j=0
	for i in range(r):
		for j in range(c):
			if max_s<s[i][j]:
				max_s=s[i][j]
				max_i=i
				max_j=j
	for i in range(max_i,max_i-max_s,-1):
		for j in range(max_j,max_j-max_s,-1):
			print(ar[i][j],end=" ")
		print("")
main()
