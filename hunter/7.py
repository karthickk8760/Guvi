k=int(input())
print("0" if k>0 and (k & (k-1))==0 else "1")
