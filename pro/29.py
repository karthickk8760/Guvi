def main():
	l=range(10)
	c=0
	r=[]
	n=int(input())
	for i in l:
		for j in l:
			v=i*10+j
			if i+j+v==n:
				r.append(v)
				c=c+1
	print(c)
	for i in r:
		print(i)
main()
