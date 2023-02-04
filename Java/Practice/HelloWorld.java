import java.util.*;

public class HelloWorld {
    public static void main(String[] args) {
        /*
         * string.repeat(count)
         * String s = "Is that point clear to you class?";
         * char ch[] = new char[9];
         * s.getChars(14, 20, ch, 0);
         * for (char c : ch)
         * System.out.print(c);
         * System.out.println("sir");
         */
        // String s = "January";
        // System.out.println(args[0].substring(1, args[0].length() - 1));
        // System.out.println("\u0026");
        var s1 = "boxer";// args[0];

        System.out.println(s1);
    }

    public static int randNum(int range) {
        return (int) (Math.random() * 5);
    }

    static int stringCount(String s, String t) {
        int count = 0, i = s.length();
        while (s.lastIndexOf(t, i) != -1) {
            i = s.lastIndexOf(t, i) - t.length();
            count++;
        }
        return count;
    }

    public static String CapitalizeFirstLetter(String s) {
        String[] s1 = s.split(" ");
        String s2 = "";
        for (String v : s1)
            s2 += v.substring(0, 1).toUpperCase() + v.substring(1, v.length()) + " ";
        return s2;
    }

    public static String binaryIp(String s) {
        String binStr = "";
        String[] arr = s.split("[.]");

        if (arr.length > 4)
            System.out.println("Wrong IP Address");
        else {
            for (String a : arr) {
                int eachNum = Integer.parseInt(a);
                if (eachNum < 0 || eachNum > 255) {
                    System.out.println("Wrong IP Address");
                    return "";
                } else
                    binStr += Integer.toBinaryString(eachNum) + " ";
            }
        }
        return binStr;
    }

}