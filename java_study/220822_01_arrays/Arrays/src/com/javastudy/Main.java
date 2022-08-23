package com.javastudy;

import java.util.Scanner;

public class Main {
    // https://www.udemy.com/course/java-the-complete-java-developer-course/learn/lecture/3323780#overview

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int[] myArray01 = new int[10];

        myArray01[5] = 50;

        double[] myArray02 = new double[10];
        myArray02[0] = 9;
        System.out.println(myArray02[0]);

        int[] myArray03 = {1, 2, 3, 4, 5};

        System.out.println(myArray03);
        System.out.println(myArray02);

        int[] myArray04 = new int[13];

        for (int i = 0; i < myArray04.length; i++) {
            myArray04[i] = i * 20;
        }
        for (int i = 0; i < myArray04.length; i++) {
            System.out.println(myArray04[i]);
        }

        printArray(myArray03);

        int[] inputsScanner = getIntegers(5);

        printArray(inputsScanner);

        System.out.println("The average of the inputed numbers is "+calculateAverage(inputsScanner));
    }

    public static void printArray(int[] anArray) {
        System.out.print("[");
        for (int i = 0; i < anArray.length - 1; i++) {
            System.out.print(anArray[i] + ", ");
        }
        System.out.print(anArray[anArray.length - 1]);

        System.out.println("]");
    }


    public static int[] getIntegers(int number) {
        System.out.println("Enter " + number + " integer values.\r");
        int[] values = new int[number];

        for (int i = 0; i < values.length; i++) {
            System.out.print("> ");
            values[i] = scanner.nextInt();
        }

        return values;
    }

    public static double calculateAverage(int[] array) {
        int sum = 0;

        for (int i = 0; i < array.length; i++) {
            sum += array[i];
        }

        return (double) sum / (double) array.length;
    }

}
