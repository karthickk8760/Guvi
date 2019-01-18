n=int(input())
li=[]
counte=[]
for i in range(n):
    k=int(input())
    li.append(k)
for num in li:
    counte.append(li.count(num))
print(max(counte))
