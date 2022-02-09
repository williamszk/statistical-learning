public class Main {

    public static void main(String[] args) {
        for (int i = 2; i <= 5; i++){
            int interestRate = i;
            System.out.println("10,000 at " + interestRate +"% interest = " + calculateInterest(10000.0, interestRate));
        }
    }

    // In Java and Go differently from C and C++ we can write the methods in other places instead 
    // of before the main function

    public static double calculateInterest(double amount, double interestRate) {
        return (amount * (interestRate/100));
    }


}

