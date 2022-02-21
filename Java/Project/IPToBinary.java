import java.util.Scanner;

//Coded by Subhadeep Mandal
public class IPToBinary {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        String[] arr = s.split("[.]");

        if (arr.length > 4)
            System.out.println("Wrong IP Address");
        else {
            for (String a : arr) {
                int eachNum = Integer.parseInt(a);
                if (eachNum < 0 || eachNum > 255) {
                    System.out.println("Wrong IP Address");
                    break;
                } else
                    System.out.print(Integer.toBinaryString(eachNum) + " ");
            }
        }

        sc.close();
    }
}
