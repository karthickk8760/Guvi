st=raw_input()
a=[0]*256
maxi=-1
for x in st:
	a[ord(x)]+=1
for x in st:
	if maxi<a[ord(x)]:
		ans=x
print(ans)
