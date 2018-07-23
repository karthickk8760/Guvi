n=int(input());
k=int(input());
li=[];
for i in range(0,n):
    el=input();
    li.append(el);
li.sort();
for i in li:
    if int(i)<k:
        print(i);
