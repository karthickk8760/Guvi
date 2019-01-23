n=int(input())
k=int(input())
li=[]
sum=0
while n!=0:
    r=n%10
    li.append(r)
    n=n//10
for i in range(k+1):
    if i in li:
        sum+=1
if sum==k:
    print("Yes")
else:
    print("No")
