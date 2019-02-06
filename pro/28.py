n=int(input("How many people"))
a=[]
print("Enter their Waiting time")
for x in range(n):
	k=int(input())
	a.append(k)
a.sort()
ans=0
c=1
for x in range(1,n):
	ans=ans+a[x-1]
	if ans>a[x]:
		continue
	else:
		c+=1
print(c)
