//HackerRank Java Output Fotmatting
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
            Scanner sc=new Scanner(System.in);
            System.out.println("================================");
            for(int i=0;i<3;i++){             //Runs 3 times increase to the number of times you want
                String s1=sc.next();
                int x=sc.nextInt();
                while(s1.length() < 15)
                    s1+=" ";
                    
                String numstr = String.valueOf(x);
                while(numstr.length() < 3)
                    numstr = "0"+numstr;
                    
                s1+=numstr;
                System.out.println(s1);
            }
            System.out.println("================================");

    }
}
