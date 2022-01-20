/* String str
str.equals("something")
*/

public class IsWorkingDay {
        public static void main(String[] args) {
                if (args[0].equals("Sunday"))
                        System.out.println("Holiday");
                else
                        System.out.println("Working Day");

        }
}
