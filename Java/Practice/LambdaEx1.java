interface Number {
    int m1(int a);
}

class LambdaEx1 {

    public static void main(String args[]) {

        Number cube = a -> a * a * a;
        System.out.println("The cube is : " + cube.m1(4));
        Number area = a -> {
            System.out.println("Calculating area...");
            return a * a;
        };
        System.out.println("The area of square is : " + area.m1(6));
    }

}