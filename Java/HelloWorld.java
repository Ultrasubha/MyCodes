import java.util.*;
class HelloWorld {
    public static void main(String[] args) throws Exception {
        String arr[] = {"hi","hello","world"};
        Arrays.sort(arr);
        for(String str : arr)
            System.out.println(str);
        String ar[] = new String[3];
        ar[0] = "his";
        ar[1] = "her";
        ar[2] = "there";
        System.out.println(ar[1]);
    }
}