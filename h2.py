a = input()
b=[]
ans = []
for i in range(0,a):
    d=input()
    b.append(d)
b.sort()
for i in range(len(b)-1,-1,-1):
    ans.append(b[i])

print ''.join(map(str,ans))
