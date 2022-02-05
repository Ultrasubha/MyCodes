/*MY SOLUTION for---
 *https://www.codechef.com/FEB221C/problems/BINBASBASIC
 */
import java.util.*;
import java.lang.*;
import java.io.*;

class BinaryBase {
    public static void main(String[] args) throws java.lang.Exception {
        Scanner scan = new Scanner(System.in);
        int N = 0, K = 0;
        String S = "";
        int T = scan.nextInt();
        scan.nextLine();

        for (int t = 0; t < T; t++) {
            N = scan.nextInt();
            K = scan.nextInt();
            scan.nextLine();
            S = scan.nextLine();

            if (isPalindrome(S, N, K))
                System.out.println("YES");
            else
                System.out.println("NO");
        }
        scan.close();
    }

    static boolean isPalindrome(String str, int N, int K) {
        int i = 0, j = str.length() - 1, count = 0;

        while (i < j) {

            // Mismatch
            if (str.charAt(i) != str.charAt(j))
                count++;

            i++;
            j--;
        }

        if (count == K)
            return true;
        else if (count > K)
            return false;
        else {
            K -= count;
            if (K % 2 == 0)
                return true;
            else {
                if (N % 2 == 0)
                    return false;
                else
                    return true;
            }
        }
    }
}
