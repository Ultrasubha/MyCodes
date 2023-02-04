interface I1 {

    int sum(int a, int b);

}

interface I2 extends I1 {

    int subtract(int a, int b);
}

interface I3 {
    int multiply(int a, int b);
}

class Interface2 implements I2, I3 {
    public int sum(int a, int b) {
        return a + b;
    }

    public int subtract(int a, int b) {
        return a - b;
    }

    public int multiply(int a, int b) {
        return a * b;
    }

    public static void main(String args[]) {
        Interface2 mo = new Interface2();

        I3 i3 = mo;
        I2 i2 = mo;
        System.out.println(i3.multiply(2, 3));
        System.out.println(i2.sum(2, 3));
        // I3 i23= new I3(); cannot be instantiated

        I3 i33 = new Interface2();
    }
}