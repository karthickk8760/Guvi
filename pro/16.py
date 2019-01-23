def max(l):
	m=-1
	for i in l:
		if m<i:
			m=i
	print(m)
	return m
  
def main():
	d=int(input())
	l=[]
	f=0
	for i in range(d):
		l.append(int(input()))
	m=max(l)
	print(m+d)
  
main()
