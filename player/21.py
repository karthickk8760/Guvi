import math
    x1=int(input("X1 value:"))
    y1=int(input("Y1 value:"))
    x2=int(input("X2 value:"))
    y2=int(input("Y2 value:"))
    x3=int(input("X3 value:"))
    y3=int(input("Y3 value:"))
    a1=x2-x1
    b1=y2-y1
    a2=x3-x2
    b2=y3-y2
    a3=x3-x1
    b3=y3-y1
    d1=math.sqrt(a1*a1+b1*b1)
    d2=math.sqrt(a2*a2+b2*b2)
    d3=math.sqrt(a3*a3+b3*b3)
    if(d3==(d1+d2)):
	   print("Yes")
    else:
	   print("No")
