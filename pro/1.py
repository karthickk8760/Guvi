def longcomstr(l):
	c=l[0]
	s=''
	n=len(c)
	for i in range(1,len(l)):
		for j in range(0,len(l) and n):
			if c[j]!=l[i][j]:
				break
			s=s+c[j]
	print(s)
def main():
	try:
		strarr=raw_input()
		l=strarr.split()
		longcomstr(l)
	except:
		print('invalid')
