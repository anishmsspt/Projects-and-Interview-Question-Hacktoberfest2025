import java.io.*;
import java.util.*;
   
    
    public class sumofsubsets {

        static void helper(int[] arr,int idx,ArrayList<Integer> li,List<ArrayList> ans,int tgt){
        
        if(idx>=arr.length && tgt!=0) return;
        if(tgt<0) return;
        if(tgt==0){
            ans.add(new ArrayList<>(li));
            return;
        }
        li.add(arr[idx]);
        helper(arr,idx+1,li,ans,tgt-arr[idx]);
        li.remove(li.size()-1);
        helper(arr,idx+1,li,ans,tgt);
    }


        public static void main(String[] args) {
        
         Scanner sc=new Scanner(System.in);
         int n=sc.nextInt();
         int[] arr=new int[n];
         for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }
         int tgt=sc.nextInt();
        
         ArrayList <Integer> li=new ArrayList<>();
         List<ArrayList> ans=new ArrayList <>();
         helper(arr,0,li,ans,tgt);
         for(int i=0;i<ans.size();i++){
            for(int j=0;j<ans.get(i).size();j++){
                System.out.print(ans.get(i).get(j)+","+" ");
            }
            System.out.println('.');
        }
        sc.close();
    
    }

}

