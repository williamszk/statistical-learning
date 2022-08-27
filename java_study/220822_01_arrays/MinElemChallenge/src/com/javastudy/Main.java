package com.javastudy;

// https://www.udemy.com/course/java-the-complete-java-developer-course/learn/lecture/10671286#overview

import java.util.Scanner;

public class Main {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {

        int[] array1 = readIntegers(5);

        int minVal = findMin(array1);

        System.out.println("The minimum value is: " + minVal);
    }

    public static int[] readIntegers(int capacity) {

        int[] array = new int[capacity];
        System.out.println("Enter " + capacity + " integer values:\r");
        for (int i = 0; i < array.length; i++) {
            array[i] = scanner.nextInt();
        }

        return array;
    }

    public static int findMin(int[] array) {
        int min = array[0];
        for (int i = 0; i < array.length; i++) {
            if (array[i] < min) {
                min = array[i];
            }
        }
        return min;
    }
}
