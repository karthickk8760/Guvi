def main():
	n=int(input())
	l=list(map(int,input().split()))
	for i in range(n):
		prev=l[i]
		co=1
		for j in range(i+1,n):
			if prev >0 and l[j]<0:
				co+=1
			elif prev<0 and l[j]>0:
				co+=1
			prev=l[j]
		print(co,end=" ")
main()
