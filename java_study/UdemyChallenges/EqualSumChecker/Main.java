public class Main {
    public static void main(String[] args) {
        testMethodHasEqualSum(1,1,1, false);
        testMethodHasEqualSum(1,1,2, true);
        testMethodHasEqualSum(1,-1,0, true);
    }

    public static void testMethodHasEqualSum(int number1, int number2, int result, boolean expectedResponse) {
        boolean testResponse = false;
        testResponse = hasEqualSum(number1, number2, result) == expectedResponse;
        System.out.println(testResponse);
    }

    public static boolean hasEqualSum(int number1, int number2, int result) {
        boolean response = false;
        response = number1 + number2 == result;
        return response;
    }

}