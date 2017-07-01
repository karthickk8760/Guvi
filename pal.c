#include<stdio.h>
int main()
{
 int a,b,c=0,d;
 scanf("%d",&a);
 a=d;
 while(a!=0)
 {
  b=a%10;
  c=b+(c*10);
  a=a/10;
  }
  if(d==c)
  printf("Palindrome");
  else
  printf("Not a Palindrome");
  return 0;
  }
 
