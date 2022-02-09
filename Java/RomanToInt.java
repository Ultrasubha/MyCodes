//Coded by Subhadeep Mandal
public class RomanToInt {
    public static void main(String[] args) {
        String s = "III";
        int len = s.length();
        int num[] = new int[len];
        int finalNum = 0;

        // Making array out of the given Roman chars
        for (int i = 0; i < len; i++) {
            switch (s.charAt(i)) {
                case 'I':
                    num[i] = 1;
                    break;
                case 'V':
                    num[i] = 5;
                    break;
                case 'X':
                    num[i] = 10;
                    break;
                case 'L':
                    num[i] = 50;
                    break;
                case 'C':
                    num[i] = 100;
                    break;
                case 'D':
                    num[i] = 500;
                    break;
                case 'M':
                    num[i] = 1000;
                    break;
                default:
                    System.out.println("Wrong input");
            }
        }

        // Weeding out the subtraction areas
        for (int i = 0; i < len - 1; i++)
            if (num[i] != 0 && num[i] < num[i + 1]) {
                num[i + 1] -= num[i];
                num[i] = 0;
            }

        // Adding up to get a decimal number
        for (int v : num)
            finalNum += v;

        System.out.print(finalNum);
    }
}
