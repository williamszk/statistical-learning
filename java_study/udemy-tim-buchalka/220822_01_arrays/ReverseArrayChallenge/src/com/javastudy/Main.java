package com.javastudy;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {

        int[] array = {1, 2, 3, 4, 5, 6};
        System.out.println("Before: " + Arrays.toString(array));
        reverse(array);
        System.out.println("After: " + Arrays.toString(array));

        int[] array2 = {2,3,1,5, 4, 5, 6, 8, 9};
        System.out.println("Before: " + Arrays.toString(array2));
        reverse(array2);
        System.out.println("After: " + Arrays.toString(array2));
    }

    public static void reverse(int[] array) {
        int temp;
        for (int i=0; i<array.length/2; i++){
            temp = array[i];
            array[i] = array[array.length - i - 1];
            array[array.length - i - 1] = temp;
        }
    }
}
