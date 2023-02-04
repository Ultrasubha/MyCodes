public class IndexFinder {
    public int printIndex(int[] intArr, int element) {
        int num = 0;
        boolean a = false;
        for (int i = 0; i < intArr.length; i++)
            if (i == element && !a) {
                a = true;
                num = i;
            }
        return num;
    }
}