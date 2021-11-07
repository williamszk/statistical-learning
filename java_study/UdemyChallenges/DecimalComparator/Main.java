// https://www.udemy.com/course/java-the-complete-java-developer-course/learn/quiz/4441294#overview

public class Main {
    
    public static void main(String[] args) {
        
        testMethodAreEqualByThreeDecimalPlaces(-3.1756, -3.175, true);
        testMethodAreEqualByThreeDecimalPlaces(3.175, 3.176, false);
        testMethodAreEqualByThreeDecimalPlaces(3.0, 3.0, true);
        testMethodAreEqualByThreeDecimalPlaces(-3.123, 3.123, false);
    }

    public static void testMethodAreEqualByThreeDecimalPlaces(double number1, double number2, boolean expectedOutput) {
        boolean response = areEqualByThreeDecimalPlaces(number1, number2) == expectedOutput;
        System.out.println(response);
    }

    public static boolean areEqualByThreeDecimalPlaces(double number1, double number2) {
        boolean response = false;

        int number1Int = (int) (number1*1000);
        int number2Int = (int) (number2*1000);

        response = number1Int == number2Int;

        return response;
    }

}