import java.util.Scanner;

interface shape {
    double l = 0, b = 0;

    double area();
}

class Rectangle extends shape {
    Rectangle(double l, double b) {
        this.l = l;
        this.b = b;
    }

    double area() {
        return l * b;
    }
}

class Triangle extends shape {
    Triangle(double l, double b) {
        this.l = l;
        this.b = b;
    }

    double area() {
        return l * b * 0.5;
    }
}

/*
 * class Circle extends shape {
 * Circle(double a) {
 * this.l = a;
 * }
 * 
 * double area() {
 * return (Math.PI * l * l);
 * }
 * }
 */

public class RoughWork {
    public static void main(String[] args) {
        Rectangle r1 = new Rectangle(10, 5);
        System.out.println(r1.area());
    }
}
