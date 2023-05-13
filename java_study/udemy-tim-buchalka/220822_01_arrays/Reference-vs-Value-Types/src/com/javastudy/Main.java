package com.javastudy;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {

        int myInt = 10;
        int anotherInt = myInt;

        System.out.println("myInt = " + myInt);
        System.out.println("anotherInt = " + anotherInt);

        anotherInt++;
        System.out.println("myInt = " + myInt);
        System.out.println("anotherInt = " + anotherInt);
        // int is called a value type, it does not have reference

        int[] myArr = {1, 2, 3, 4};
        int[] myArr2 = myArr;
        // arrays are called reference types
        // the operation of = will create another reference to an underlying object
        // that lives in memory
        // both myArr and myArr2 reference the same object

        System.out.println("original myArr = " + Arrays.toString(myArr));
        System.out.println("original myArr = " + Arrays.toString(myArr2));

        myArr2[0] = 99;
        // a change in of the references will change all of the references
        System.out.println("after change myArr = " + Arrays.toString(myArr));
        System.out.println("after change myArr = " + Arrays.toString(myArr2));

        // we can pass arrays by reference into functions
        // in Go, slices are passed by reference?
        // no in Go everything is passed by value
        // the slice is special type of pointer, with more properties
        // we could argue that reference types are also a special
        // kind of pointer too
        // but in the case of Go, we also have the concept of pointers, referencing
        // and de-referencing

        modifyMyArray(myArr);
        System.out.println("after running modifyMyArray myArr = " + Arrays.toString(myArr));
        System.out.println("after running modifyMyArray myArr = " + Arrays.toString(myArr2));

        // we can also create a new reference to the same variable
        // this is called dereferencing a variable
        myArr2 = new int[]{0,0,0,0,0,0,0,0};
        System.out.println("after dereferencing myArr2 myArr = " + Arrays.toString(myArr));
        System.out.println("after dereferencing myArr2 myArr = " + Arrays.toString(myArr2));
        // a new object is created, as the new indicates


        // is String a reference type?
        String myStr = "hello there";
        String myStr2 = myStr;
        System.out.println("original myStr = " + myStr);
        System.out.println("original myStr2 = " + myStr2);

        myStr = "good bye";
        System.out.println("after change myStr = " + myStr);
        System.out.println("after change myStr2 = " + myStr2);
        // strings are not reference types, they are value types

    }

    public static void modifyMyArray(int[] arr) {
        arr[0]  = 99999;
    }

}
