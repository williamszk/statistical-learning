package com.javastudy;
// https://www.udemy.com/course/java-the-complete-java-developer-course/learn/lecture/3323782#overview
import java.util.Arrays;
import java.util.Scanner;

public class Main {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {

        int[] myIntegers = getIntegers(5);

        System.out.println("Original Array:");
        printArray(myIntegers);
        int[] sortedArray = sortIntegers(myIntegers);
        System.out.println("After Sorting:");
        printArray(sortedArray);

    }


    public static int[] getIntegers(int capacity) {

        int[] array = new int[capacity];
        System.out.println("Enter " + capacity + " integer values:\r");
        for (int i = 0; i < array.length; i++) {
            array[i] = scanner.nextInt();
        }

        return array;
    }

    public static void printArray(int[] arr) {
        System.out.print("[");
        for (int i = 0; i < arr.length - 1; i++) {
            System.out.print(arr[i] + ", ");
        }
        System.out.println(arr[arr.length - 1] + "]");
    }

    public static int[] sortIntegers(int[] array) {
//        int[] sortedArray = new int[array.length];
//        System.arraycopy(array, 0, sortedArray, 0, array.length);
        int[] sortedArray = Arrays.copyOf(array, array.length);

        boolean flag = true;
        int temp;

        while (flag) {
            flag = false;
            for (int i = 0; i < sortedArray.length - 1; i++) {
                if (sortedArray[i] < sortedArray[i + 1]) {
                    temp = sortedArray[i];
                    sortedArray[i] = sortedArray[i + 1];
                    sortedArray[i + 1] = temp;
                    flag = true;
                }
            }
        }

        return sortedArray;
    }

}
