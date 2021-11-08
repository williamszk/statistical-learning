public class Main {
    public static void main(String[] args){
        int result = 1 + 2;
        System.out.println("result = " + result);
        // assignment operator =; <-
        // expresions can be evaluated into some value
        // if we type 3, is this an expression? yes a believe so
        // in: 1 + 2
        // + is an operator
        // 1 and 2 are operands
        // and 1 + 2 is an expression
        // = and + are both operators
        
        // this will sum 1 into the variable result
        result++;
        
        // this will sum 2 into the variable result;
        result += 2;

        // subtract -1 into result
        result--;

        // multiply result by 10
        result *= 10;

        // update result by dividing it by 3
        result /= 3;

        // subtract 2 from result;
        result -= 2;

        // control flow statements
        // if-then statement

        boolean isAlien = false;
        // difference between assignment operator
        // and equals operator

        if (isAlien == false) {
            System.out.println("It is not an Alien.");
        }
        // we can write if then statements without a code block
        // but it is less clear
        // we should always use a code block

        // logical operators
        // and, or, xor, not,

        int topScore = 80;
        if (topScore == 100){
            System.out.println("You got the high score!");
        }

        int secondTopScore = 60;
        if (topScore > secondTopScore && topScore < 100) {
            System.out.println("Greater than second top score and less than 100.");
        }

        // operator precedence
        // the difference between bitwise operators and logical operators
//        int result1 = 1 | 0;
//        int result1 = 2 | 0;
//        int result1 = 3 & 2;
//        System.out.println("result1: " + result1);

        if (topScore > 90 || secondTopScore <= 90) {
            System.out.println("Either or both of the conditions are true.");
        }

//        boolean isCar = true;
//        if (isCar = true) {
//            System.out.println("I ran here!");
//        }
        boolean isCar = true;
        boolean wasCar = isCar ? true : false;
        System.out.println("wasCar = " + wasCar);

        boolean isClientEligible = false;
        String messageEligible = isClientEligible ? "Client is eligible." : "Client is NOT eligible.";
        System.out.println(messageEligible);

//        int myXorTest = 1 ^ 1;
//        int myXorTest = 1 ^ 0;
        int myXorTest = 0 ^ 0;
        System.out.println("myXorTest = " + myXorTest);

        double myValue1 = 20.0d;
        double myValue2 = 80.0d;
        double myRemainder1 = ((myValue1 + myValue2)*100) % 40.0d;
//        System.out.println((myValue1 + myValue2)*100/40);
//        System.out.println("myRemainder1 = " + myRemainder1);
        boolean isRemainderZero = (myRemainder1 == 0) ? true : false;
        System.out.println("isRemainderZero = " + isRemainderZero);
        if (isRemainderZero) {
            System.out.println("Didn't get any remainder.");
        } else {
            System.out.println("Got any remainder.");
        }





        
        
    }
}































