def gcd(a,b):
	if (a == 0 or b == 0):
			False
	if (a == b):
		return a
	if (a > b):
		return gcd(a-b, b)
	return gcd(a, b-a)
a,b=input(),input() 
if(gcd(a, b)):
	print(gcd(a,b))
