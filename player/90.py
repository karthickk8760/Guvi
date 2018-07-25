def fact(n):
    ft=1;
    i=1;
    while i<=n:
        ft=ft*i;
        i+=1;
    return ft;
a=int(input());
b=int(input());
per=fact(a)//(fact(a-b)*fact(b));
print(per);
