#include<stdio.h>
int main()
{
 int a,b=0,c=1,d,co=1;
 scanf("%d",&a);
 while(co<=5)
 {
printf("%d",b);
d=b+c;
b=c;
c=d;
co++;
}
return 0;
}
