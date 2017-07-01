#include<stdio.h>
int main()
{
 int a,b,c,d;
 scanf("%d",&a);
 while(a!=0)
 {
  b=a%10;
  c=c+(a*a*a);
  a=a/10;
  }
  if(d==c)
  printf("armstrong number");
  else
   printf("not an armstrong number");
   return 0;
   }
