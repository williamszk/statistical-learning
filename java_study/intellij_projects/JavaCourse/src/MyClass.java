public class MyClass {
    
    public static void main(String[] args){
        System.out.println("Hello World!");
        System.out.println("I am working!");

        long myLongValue = 100L;

        long myMinLongValue = Long.MIN_VALUE;
        long myMaxLongValue = Long.MAX_VALUE;
        System.out.println("myMinLongValue = " + myMinLongValue);
        System.out.println("myMaxLongValue = " + myMaxLongValue);

        int myTotal = (int) (myMaxLongValue/2);
//        System.out.println("myTotal = " + myTotal);

        long myTotal2 = (myMaxLongValue/2);
//        System.out.println("myTotal2 = " + myTotal2);

        byte firstNumber = 100;
        short secondNumber = 230;
        int thirdNumber = 980821;
        long forthNumber = 50_000L + 10L * (firstNumber + secondNumber + thirdNumber);

        System.out.println("forthNumber = " + forthNumber);





    }
}
