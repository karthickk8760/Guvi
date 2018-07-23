n=int(input());
li=[];
for i in range(0,n):
    el=input();
    li.append(el);
li.sort();
for i in li:
    if int(i)<n:
        print(i);
