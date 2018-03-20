a=raw_input()
a=list(a)
b=[]
for c in a:
    d=chr(ord(c)+3)
    b.append(d)
e="".join(b)
print(e)
