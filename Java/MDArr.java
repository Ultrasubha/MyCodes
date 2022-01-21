public class MDArr {
    public static void main(String[] args) {

        char st[][] = new char[3][3];
        int z = 65;

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                z++;
                st[i][j] = (char) z;
            }
        }

        for (char i[] : st) {
            for (char j : i) {
                System.out.print("Output :" + j + "\t");
            }
        }
    }
}