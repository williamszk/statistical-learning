package com.javastudy;

import java.util.Arrays;

// https://www.udemy.com/course/java-the-complete-java-developer-course/learn/quiz/5088046#overview
public class Main {

    public static void main(String[] args) {

        int[] inputArr = {106, 26, 81, 200, 5, 15};

        SortedArray sortedArray = new SortedArray();
        System.out.println("================ Original Array ====================================");
        sortedArray.printArray(inputArr);
        int[] outputArr = sortedArray.sortIntegers(inputArr) ;
        System.out.println("================ Sorted Array ====================================");
        sortedArray.printArray(outputArr);

        System.out.println("================ Expected Array ====================================");
        int[] outputArrExp = { 200, 106, 81, 26, 15, 5  } ;
        sortedArray.printArray(outputArrExp);

        System.out.println("\n\nIs the result equal to the expected? " + Arrays.equals(outputArr, outputArrExp));
    }


}
