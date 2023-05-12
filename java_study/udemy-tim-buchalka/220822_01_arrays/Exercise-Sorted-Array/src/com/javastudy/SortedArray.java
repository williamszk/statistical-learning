package com.javastudy;

import java.util.Arrays;
import java.util.Scanner;

public class SortedArray {

    private static Scanner scanner = new Scanner(System.in);

    public static int[] getIntegers(int number) {
        System.out.println("Enter " + number + " integer values.\r");
        int[] values = new int[number];

        for (int i = 0; i < values.length; i++) {
            System.out.print("> ");
            values[i] = scanner.nextInt();
        }

        return values;
    }


    public static void printArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.println("Element " + i + " contents " + arr[i]);
        }
    }

    public static int[] sortIntegers(int[] arr) {
        // implement bubble sort here
        int[] arrOut = Arrays.copyOf(arr, arr.length);

        int temp;
        boolean keepWhile = true;
        while (keepWhile) {
            for (int i = 0; i < arrOut.length - 1; i++) {
                if (arrOut[i] < arrOut[i + 1]) {
                    // swap i and i+1
                    temp = arrOut[i];
                    arrOut[i] = arrOut[i + 1];
                    arrOut[i + 1] = temp;
                    break;
                } else if (i == arrOut.length - 2) {
                    keepWhile = false;
                    break;
                }
            }
        }

        return arrOut;
    }

}
