def lcm(a,b):
    if(a>b):
        g=a
    else:
        g=b
    while(True):
        if(g%a==0 and g%b==0):
            l=g
            break
        g=g+1
    return l
a,b=input(),input() 
if(lcm(a, b)):
	print(lcm(a,b))
