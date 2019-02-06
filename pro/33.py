def substr():
	str=input()
	s=''
	out=''
	max=1
	for i in range(len(str)):
		s+=str[i]
		for j in range(i+1,len(str)):
			if ord(str[i]) > ord(str[j]):
				s+=str[j]
			else :
				break

		if max<len(s):
			max=len(s)
			out+=s
		s=''
	print(out)
substr()
