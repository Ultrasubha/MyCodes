public class Armstrong {

        public static int exponent(int len,int remainder) {
                int value=1;
                while(len>0){value*=remainder; len--;}
                return value;
        }

        public static void main(String []args) {
                int num = Integer.parseInt(args[0]);
                int len = args[0].length();
                int tempo=num,remainder,sum=0;

                while(tempo>0){
                        remainder = tempo%10;
                        tempo/=10; //progress to next higher
                        sum +=exponent(len,remainder);
                }

                if(num == sum) System.out.println("The given number " + num + " is an armstrong number");
                else System.out.println("The given number " + num + " is not an armstrong number");
        }
}
