import java.util.*;

public class getstairspath{

     static ArrayList <String> ans=new ArrayList <>();
    public static void path(int stairs,int n,String p){
        if(stairs>=n){
            if(stairs==n)
                ans.add(p);
            return ;
        }
        path(stairs+1,n,p+"1");
        path(stairs+2,n,p+"2");
        path(stairs+3,n,p+"3");
    }

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        
        path(0,n,"");
        
        System.out.println(ans);
        sc.close();
    }

}