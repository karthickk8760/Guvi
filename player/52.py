n=int(input());
k=int(input());
elements=[];
for i in range(n):
    e=int(input());
    elements.append(e);
elements.sort();
if(k<len(elements)) and k>=1:
    print(elements[k-1]);
