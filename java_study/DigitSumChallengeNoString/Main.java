public class Main {
    public static void main(String[] args) {
        System.out.println(sumDigits(22));
        System.out.println(sumDigits(34));
    }

    public static int sumDigits(int number){
        if (number >= 10){
            int totalSum = 0;
            int divisor = 10;
            int numberHold = number;
            while (numberHold > 0) {
                int digit = numberHold % divisor;
                totalSum += digit;
                numberHold = numberHold / divisor;
            }
            return totalSum;
        } else {
            return -1;
        }
    }

}
