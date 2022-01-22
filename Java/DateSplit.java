import java.util.Scanner;

public class DateSplit {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        String dt_arr[] = s.split("-");

        for (String st : dt_arr)
            System.out.println(st);
    }
}