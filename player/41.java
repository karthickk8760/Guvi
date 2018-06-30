import java.io.*;
import java.util.*;
public class MyClass {
    public static void main(String args[]) {
        int x,y;
        Scanner sc=new Scanner(System.in);
        x=sc.nextInt();
        y=sc.nextInt();
        if(x%y==0)
            System.out.println("yes");
        else
            System.out.println("no");
       
    }
}
