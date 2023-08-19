import java.util.*;

class A {
    A(){
        System.out.println("I am A");
    }
}

class B extends A{
    B(){
        System.out.println("I am B");
    }
}

class prac {
    public static void main(String[] args) {
        /*Scanner sc = new Scanner(System.in);
        Integer i = sc.nextInt();
        sc.close();*/
        //A a = new A();
        new A();
        //System.out.println(i);
    }
}