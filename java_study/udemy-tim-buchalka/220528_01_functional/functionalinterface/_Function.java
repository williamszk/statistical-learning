package functionalinterface;

import java.util.function.Function;

// javac functionalinterface/_Function.java
// java functionalinterface/_Function

public class _Function {
    private static final String BiFunction = null;

    public static void main(String[] args) {
        int num1 = incrementByOne(1);
        System.out.println("Usual Way: " + num1);

        int num2 = incrementByOneFunction.apply(1);
        System.out.println("From Function: " + num2);

        int num3 = multiplyBy10Function.apply(num2);
        System.out.println("From Function Multiply by 10: " + num3);

        // combine the two functions together
        Function<Integer, Integer> addBy1AndThenMultiplyBy10 = incrementByOneFunction
                .andThen(multiplyBy10Function);

        int num4 = addBy1AndThenMultiplyBy10.apply(1);
        System.out.println("From combined functions add 1 and mult by 10: " + num4);

        int num5 = incrementByOneFunction.andThen(multiplyBy10Function).apply(1);
        System.out.println("From combined functions add 1 and mult by 10 without defining another function: " + num5);

        int num6 = incrementByOneAndMultiply(1, 10);
        System.out.println("incrementByOneAndMultiply: " + num6);

    }

    static Function<Integer, Integer> incrementByOneFunction = number -> number + 1;
    // the arrow function here is called a lambda

    // What is the difference between the Predicate and the Function?

    static Function<Integer, Integer> multiplyBy10Function = number -> number * 10;

    static int incrementByOne(int number) {
        return number + 1;
    }

    static int incrementByOneAndMultiply(int number, int numToMultiplyBy) {
        return (number + 1) * numToMultiplyBy;
    }

    // The BiFunction is a Function that accepts two arguments

}
