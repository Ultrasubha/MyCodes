import java.util.Scanner;

public class MinorSelector {

    public static int modified(Scanner sc, int n, int i) {
        String reply = sc.nextLine();
        switch (reply) {
            case "Y":
                return n + i;
            case "N":
                return n - i;
            default:
                System.out.println("Invalid Input");
                return -500;
        }
    }

    public static void main(String[] args) {
        String choice = "(Y = Yes, N = No , NA = Can't say)";
        System.out.println(
                "Hi I am Subhadeep \\(^-^)/\nThe reccommendations are purely from my perspective and it in no way reflects the precise actuality.\nSo can you please answer these questions for me?\t"
                        + choice);
        Scanner sc = new Scanner(System.in);
        int subho = modified(sc, 0, 1);
        if (subho < 0)
            System.out.println("Sorry to see you go :( ");
        else {
            System.out.println("Awesome \\(^-^)/");
            int DS = 0, ST = 0, FS = 0, ML = 0, CS = 0, HS = 0, IOT = 0;
            String[] question = { "Do you like maths and statistics?" };
            int[] marks = { 2 };
            DS = modified(sc, DS, 2);
            System.out.println(DS);
        }
        sc.close();
    }
}