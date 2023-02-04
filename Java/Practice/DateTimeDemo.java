import java.time.*;
import java.util.Locale;

class DateTimeDemo {
    public static void main(String[] args) {
        ZoneId zid = ZoneId.of("Asia/Tokyo");
        LocalDate lt = LocalDate.now(zid);
        System.out.println("LocalDate: " + lt);
    }
}