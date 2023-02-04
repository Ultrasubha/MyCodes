interface TestInt { // this is a top-level interface
    public void printMe();
}

class AnonymousClass {
    public static void main(String[] args) {
        class Test implements TestInt {
            public void printMe() {
                System.out.println("an example of a normal local class");
            }
        }

        TestInt myPrinter1 = new Test();

        TestInt myPrinter2 = new TestInt() {
            public void printMe() {
                System.out.println("an example of an anonymous class");
            }
        };

        myPrinter1.printMe();
        myPrinter2.printMe();
    }
}