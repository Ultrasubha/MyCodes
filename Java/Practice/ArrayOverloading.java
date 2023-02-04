class ArrayOverloading {
    void meth1(int[]... a) {
        System.out.println("Variable arguement passing");

        for (int y[] : a)
            for (int x : y)
                System.out.print(x + " ");
    }

    public static void main(String... args) {
        ArrayOverloading ao = new ArrayOverloading();
        int a1[] = { 1, 2, 3 };
        ao.meth1(a1, new int[] { 4, 5, 6, 7 }, new int[] { 8, 9 });
        ao.meth1();
    }
}