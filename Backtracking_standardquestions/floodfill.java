import java.io.*;
import java.util.*;

public class floodfill {
    public static void path(int r,int c,int n,int m,int mat[][],String p){
        
        if(r==n-1 && c==m-1){
            System.out.println(p);
            return;
        }
           
        if(r>=n || r<0 || c>=m || c<0)
            return;
        
        if(mat[r][c]==1 || mat[r][c]==2)
            return;
        
        mat[r][c]=2;
        
        int dx[]={-1,0,1,0};
        int dy[]={0,-1,0,1};
        char str[]={'t','l','d','r'};
        
        for(int i=0;i<4;i++){
            int nr=r+dx[i];
            int nc=c+dy[i];
            
            
            path(nr,nc,n,m,mat,p+str[i]);
        }
        mat[r][c]=0;
        
    }
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
    Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int m=sc.nextInt();
        int[][] mat=new int[n][m];
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                mat[i][j]=sc.nextInt();
            }
        }
        
      path(0,0,n,m,mat,"");
      sc.close();
    }
}
