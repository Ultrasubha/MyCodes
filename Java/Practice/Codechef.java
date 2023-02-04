/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef {
    public static void main(String[] args) throws java.lang.Exception {
        Scanner scan = new Scanner(System.in);
        int T = scan.nextInt();
        scan.nextLine();
        while (T-- > 0)
            code(scan);
        scan.close();
    }

    private static void code(Scanner sc) {
        int x = sc.nextInt();
        System.out.println(x);
        sc.nextLine();
    }
}
