public class SumAndReverseNumber {
        public void sumAndReverseANumber (int number) {
                int a = number,rem,rev=0,sum=0;

                while(a>0){
                        rem = a%10;
                        a/=10;
                        sum+=rem;
                        rev=rev*10+rem;
                }

                System.out.println("Sum of digits : "+sum+"\nReverse : "+rev);
        }
}
