n=int(input())
k=int(input())
a=[]
for i in range(n):
    g=int(input())
    a.append(g)
for i in a:
    c=a.count(i)
    if c==k:
        print(i)
        break
