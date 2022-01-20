public class QuadraticRoots {
        public static void main(String[] args) {
                double a = Double.parseDouble(args[0]);
                double b = Double.parseDouble(args[1]);
                double c = Double.parseDouble(args[2]);

                double determinant = b*b - 4.0 *a*c;

                if(determinant>0.0) {
                        double x1 = -(b+Math.pow(determinant,0.5))/(2.0*a);
                        double x2 = -(b-Math.pow(determinant,0.5))/(2.0*a);
                        System.out.println("First root is : "+x2 +" Second root is : "+x1);
                }

                else if(determinant<0.0) System.out.println("Roots are imaginary");

                else {
                        double result = -b/(2.0*a);
                        System.out.println("Roots are equal and value is : "+result);
                }
        }
