class Student {

    int roll;
    String name;
    static int cnt = 0; // its copy is 1 per class

    Student() {
        roll = ++cnt;
    }

    Student(String name) {
        roll = ++cnt;
        this.name = name;
    }

    void show() {
        System.out.println(roll + " " + name + " ");
    }

    public static void main(String args[]) {
        Student s1 = new Student("Manan");
        s1.show();
        Student s2 = new Student("Aakash");
        s2.show();
        Student s3 = new Student();
        s3.show();
        Student s4 = new Student("Abhisht");
        s4.show();
        System.out.println(Student.cnt);
    }
}