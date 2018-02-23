x=raw_input()
print(any(c.isdigit for c in x))
if(any(c.isalpha for c in x) and any(c.isdigit for c in x)): 
    print("yes")
else:
    print("no")
