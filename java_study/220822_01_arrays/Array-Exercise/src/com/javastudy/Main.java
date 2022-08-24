package com.javastudy;

//  https://www.udemy.com/course/java-the-complete-java-developer-course/learn/lecture/3323782#overview
public class Main {


    public static void main(String[] args) {

        int[] myArr01 = {5, 15, 106, 26, 81};
        System.out.println("\nBefore sort:");
        printArray(myArr01);
        sortIntegers(myArr01);
        System.out.println("After sort:");
        printArray(myArr01);

        int[] myArr02 = {10, 80, 30, 90, 40, 50, 70};
        System.out.println("\nBefore sort:");
        printArray(myArr02);
        sortIntegers(myArr02);
        System.out.println("After sort:");
        printArray(myArr02);

        int[] myArr03 = {24, 15, 32, 12, 52, 46, 76, 34, 39, 64, 79, 84, 32, 74, 14, 85, 92, 61, 34, 68};
        System.out.println("\nBefore sort:");
        printArray(myArr03);
        sortIntegers(myArr03);
        System.out.println("After sort:");
        printArray(myArr03);
    }

    public static void sortIntegers(int[] arr) {
        quickSort(arr, 0, arr.length-1);
    }

    /**
     * low: Starting index
     * high: Ending index
     */
    private static void quickSort(int[] arr, int low, int high) {
        // https://www.geeksforgeeks.org/quick-sort/
        if (low < high) {
            // pi is the partition index,
            // arr[pi] is now at the right place
            int pi = partitionDesc(arr, low, high);

            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    /**
     * This function takes last element as pivot, places the pivot element at its correct position in sorted array,
     * and places all smaller (smaller than pivot) to the left of the pivot and all greater elements to the
     * right of pivot.
     */
    private static int partitionDesc(int[] arr, int low, int high) {

        // pivot (Element to be placed at right position)
        int pivot = arr[high];

        // Index of the largest element and indicates the right position of pivot found so far
        int i = (low - 1);

        for (int j = low ; j <= high - 1; j++) {
            // if current element is smaller than the pivot
            if (arr[j] >= pivot) {
                i++; // increment index of largest element
                // swap arr[i] and arr[j]
                swapElem(arr, i, j);
            }
        }
        // swap arr[i+1] and arr[high]
        swapElem(arr, i+1, high);

        return i + 1;
    }

    /**
     * Swap two element in an array.
     * */
    private static void swapElem(int[] arr,int i, int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static void printArray(int[] arr) {
        System.out.print("[");
        for (int i = 0; i < arr.length - 1; i++) {
            System.out.print(arr[i] + ", ");
        }
        System.out.println(arr[arr.length - 1] + "]");
    }

}
