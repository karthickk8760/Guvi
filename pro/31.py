def dag():
	n=int(input())
	e=int(input())
	r=[]
	l=[]
	for i in range(e):
		for j in range(2):
			r.append(int(input()))
		l.append(r)
		r=[]
	print(l)
	dict={}
	for i in range(len(l)):
		if i not in dict:
			dict[l[i][0]]=[l[i][1]]
		else :
			dict[l[i][0]].append(l[i][1])
	print(dict)
	s=0
	max=-1
	for key in dict:
		for i in range(len(dict[key])):
			s+=dict[key][i]
			if dict[key][i] in dict:
				for i in range(len(dict[dict[key][i]])):
					s+=dict[key][i]
			else :
				continue
		if max<s:
			max=s
		s=0
	print(max)
dag()
