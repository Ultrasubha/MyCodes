public class Employee {
    int empid;
    String empname;
    String designation;

    Employee() {
        empid = 101;
        empname = "Subhadeep";
        designation = "Game Developer";
    }

    Employee(int num, String name, String desg) {
        empid = num;
        empname = name;
        designation = desg;
    }

    void show() {
        System.out.println(empid + " " + empname + " " + designation);
    }

    public static void main(String[] args) {
        Student E1 = new Student();
        E1.show();
        Student E2 = new Student(12000, "Jarvis", "Janitor");
        E2.show();
    }
}