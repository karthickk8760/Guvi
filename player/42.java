import java.util.*;
import java.lang.*;
import java.util.ArrayList;
public class sortt{
    public static void main(String aa[]){
    Scanner s=new Scanner(System.in);
    int n=s.nextInt();
    ArrayList<Integer>v=new ArrayList<Integer>();
    for(int i=0;i<n;i++){
        int c=s.nextInt();
        v.add(c);
    }
    int k=Collections.min(v);
    Collections.sort(v);
    int z=v.get(0);
    if(k==z){
        System.out.println("yes");
    }
}
}
