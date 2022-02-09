/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

class Datatype {
    public static void main(String[] args) throws java.lang.Exception {
        Scanner scan = new Scanner(System.in);
        int T = scan.nextInt();
        scan.nextLine();
        while (T-- > 0)
            code(scan);
        scan.close();
    }

    private static void code(Scanner sc) {
        int limit = sc.nextInt();
        int value = sc.nextInt();
        int result = value % limit;
        sc.nextLine();

        if (value >= limit) {
            int times = value / limit;
            if (result < times)
                result = limit - times + result + 1;
            else
                result -= times;
        }

        System.out.println(result);
    }
}
