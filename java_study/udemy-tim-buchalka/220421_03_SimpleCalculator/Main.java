public class Main {
    public static void main(String[] args) {
        // https://www.udemy.com/course/java-the-complete-java-developer-course/learn/quiz/4585936#overview

        SimpleCalculator calculator = new SimpleCalculator();
        calculator.setFirstNumber(5.0);
        calculator.setSecondNumber(4);
        System.out.println("add = " + calculator.getAdditionResult());
        System.out.println("subtract = " + calculator.getSubtractionResult());
        calculator.setFirstNumber(5.25);
        calculator.setSecondNumber(0);

        System.out.println("multiply = " + calculator.getMultiplicationResult());
        System.out.println("divide = " + calculator.getDivisionResult());

    }
}
