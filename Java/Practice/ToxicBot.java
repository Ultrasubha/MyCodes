import java.util.Scanner;

public class ToxicBot {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Are you a boy or a girl? (reply 'b' or 'g')");
        char st = sc.next().charAt(0);
        String congo = "Congratulations, for confirming yourself as";

        switch (st) {
            case 'b':
                System.out.println("Do you like girls? (reply 'y' or 'n')");
                char boys = sc.next().charAt(1);
                System.out.println("Do you like boys? (reply 'y' or 'n')");
                char girls = sc.next().charAt(2);
                if (boys == 'y') {
                    if (girls == 'y')
                        System.out.println(congo + " bisexual :)");
                    else if (girls == 'n')
                        System.out.println(congo + " gay :)");
                    else
                        System.out.println(" Incorrect Input");
                }

                else if (boys == 'n') {
                    if (girls == 'y')
                        System.out.println("Why didn't you take birth as a girl then? :/");
                    else if (girls == 'n')
                        System.out.println("Do you even like anything you freak?");
                    else
                        System.out.println(" Incorrect Input");
                }

                else
                    System.out.println(" Incorrect Input");
                break;

            case 'g':
                System.out.println("Do you like boys? (reply 'y' or 'n')");
                System.out.println("Do you like girls? (reply 'y' or 'n')");
                break;
            default:
                System.out.println(" Incorrect Input");
        }
        sc.close();
    }
}