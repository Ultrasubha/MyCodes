abstract class Shape {

    double dim1, dim2;

    Shape(double dim1, double dim2) {
        this.dim1 = dim1;
        this.dim2 = dim2;
    }

    void show() {
        System.out.println(dim1 + " " + dim2);
    }

    abstract double area();
}

class Rectangle extends Shape {
    double etc;

    Rectangle(double dim1, double dim2) {
        super(dim1, dim2);
    }

    public double area() {
        return dim1 * dim2;
    }
}

class TestAbstract {
    public static void main(String args[]) {
        Rectangle r1 = new Rectangle(25, 56);
        System.out.println(r1.area());
        r1.show();
        Shape s1;
        s1 = r1;
        s1.show();
        s1.area();
        // r1.etc = 25;
        // s1.etc=20;// not allowed
    }
}