import java.io.*;
import java.util.*;

public class printsubsequences {
    static void print_seq(String s,String curr){
        
        if(s.equals("")){
            System.out.println(curr);
            return;
        }
        
        print_seq(s.substring(1),curr+s.charAt(0));
        print_seq(s.substring(1),curr);
        
    }
    public static void main(String[] args) {
        
    Scanner sc=new Scanner(System.in);
        String s=sc.next();
        print_seq(s,"");
        sc.close();
    
    }
}
