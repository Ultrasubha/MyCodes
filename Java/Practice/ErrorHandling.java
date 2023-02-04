public class ErrorHandling {
    public static void main(String... a) {
        try {
            int x = 0, result;
            result = 5 / x;
            System.out.println(result);
        } catch (Exception e) {
            System.out.println("Bal eida ki kortasos");
        } finally {
            System.out.println("Balda eida tui kamne korli?");
        }
    }
}