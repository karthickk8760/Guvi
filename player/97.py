l=int(input())
r=int(input())
sum=0
for i in range(l,r+1):
    if i%2!=0:
        sum+=i
print(sum)
