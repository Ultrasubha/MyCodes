class VariablePassing {

    void meth1(int a[], int b[]) {
        System.out.println("Contents of array a[]");
        for (int x : a)
            System.out.print(x + " ");
        System.out.println("\n");

        System.out.println("Contents of array b[]");
        for (int x : b)
            System.out.print(x + " ");
        System.out.println("\n");

        System.out.println("Sum of Contents of both arrays is:");
        for (int x = 0; x < a.length; x++)
            System.out.print((a[x] + b[x]) + " ");
    }

    public static void main(String[] args) {
        VariablePassing vp = new VariablePassing();

        int a[] = { 1, 2, 3, 4, 5 };
        vp.meth1(a, new int[] { 6, 7, 8, 9, 10 });
    }
}