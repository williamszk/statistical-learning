public class PositiveNegativeZero {

    public static void main(String[] args) {
        checkNumber(-90);
    }

    public static void checkNumber(int number) {
        String message;
        if (number > 0) {
            message = "positive";
        } else if (number < 0) {
            message = "negative";
        } else {
            message = "zero";
        }
        System.out.println(message);
    }
}
