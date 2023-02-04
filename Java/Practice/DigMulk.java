/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

class DigMulk {
    public static void main(String[] args) throws java.lang.Exception {
        Scanner scan = new Scanner(System.in);
        int T = scan.nextInt();
        scan.nextLine();
        while (T-- > 0)
            code(scan);
        scan.close();
    }

    private static void code(Scanner sc) {
        int K = sc.nextInt();
        K = sc.nextInt(); // To ignore the value of N as we don't need it
        int M = sc.nextInt();
        sc.nextLine();
        String s = sc.nextLine();

        for (int i = 0; i < M; i++) {
            s = numStr(s, K);
        }
        double d = Math.pow(10, 9) + 7;
        int ans = s.length() % (int) d;
        System.out.println(ans);
    }

    private static String numStr(String s, int K) {
        String s1 = "";
        int val = 0;
        for (int i = 0; i < s.length(); i++) {
            val = s.charAt(i) - 48;
            val *= K;
            s1 += val;
        }
        return s1;
    }
}
