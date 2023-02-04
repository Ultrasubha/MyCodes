import java.util.Scanner;

public class PrimeVerify {
    public static void main(String[] args) {
        System.out.println("Enter a number");
        Scanner scan = new Scanner(System.in);
        int number = scan.nextInt();
        scan.close();
        boolean flag = false;
        for (int i = 2; i < number; i++) {
            if (number % i == 0)
                flag = true;
        }

        if (flag == false)
            System.out.println(number + " is a prime number");
        else
            System.out.println(number + " is not a prime number");
    }
}