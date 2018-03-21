st1=raw_input()
    st=list(st1)
    for x in range(len(st)-1):
	   if st[x]==' ' and st[x+1]==" ":
	       	st[x]=''
    ans=''
    for x in st:
	   ans=ans+x
    print(ans.strip())
