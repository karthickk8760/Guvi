n=int(input())
nli=[]
while n!=0:
    r=n%10
    nli.append(r)
    n=n//10
print(nli[0]+nli[len(nli)-1])
