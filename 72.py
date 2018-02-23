a=raw_input()
b=a.lower()
d=0
v=["a","e","i","o","u"]
for c in b:
    if c in v:
        d=d+1
if(d>0):
    print("yes")
else:
    print("no")
