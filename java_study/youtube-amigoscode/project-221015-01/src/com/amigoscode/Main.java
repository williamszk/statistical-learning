package com.amigoscode;
// https://youtu.be/Qgl81fPcLc8?t=915

import java.time.LocalDate;

public class Main {

    /**
     * This is a multi line comment
     * ```
     * Is this code?
     * ```
     */
    public static void main(String[] args) {
        // write your code here
        System.out.println("Hooray my first Java code");

        int number = 100;
        String name = "Amigoscode";
        double num2 = 100.01;

        // byte is between -128 and 127
        byte theByte = (byte) 255;
        System.out.println("theByte: " + theByte); // -1

        byte theByte2 = -128;
        System.out.println("theByte2: " + theByte2);

        // this is an integer type, is it 16bits? yes 2bytes
        short theShort = 8_989;

        // how many bits are in the int?
        // it is 32 bits, 4 bytes
        int theInt = 1_231_231;

        // in the long we can store 8 bytes
        long theLong = 198_039_123L;

        // 4 bytes
        float theFloat = 123.123F;

        // 8 bytes
        double theDouble = 2_391_231_980.3123D;

        // 1 byte
        boolean isAdult = false;

        // 2 bytes
        char nameInitial = 'A';

        // variables
        // primitive types
        // primitive data types, are not reference variables
        // container variables, reference data types

        System.out.println(nameInitial);
        System.out.println(theLong);

        String name2 = "Bob Martin";
        name2.length();
        System.out.println(name2.toUpperCase());

        // there are many built-in Reference Data types
        LocalDate nowTime = LocalDate.now();
        System.out.println("local date: " + nowTime);

        // An experiment about the different between primitive data types
        // and reference data types
        int a = 10;
        int b = a; // this is passed by copy
        System.out.println("before a: " + a); // 10
        System.out.println("before b: " + b); // 10
        a = 20;
        System.out.println("after a: " + a); // 20
        System.out.println("after b: " + b); // 10
        // notice that b is not changed

        String theName = "Dennis Diffie";
        String anotherName = theName; // this is passed by copy
        System.out.println("before theName: " + theName);
        System.out.println("before anotherName: " + anotherName);
        theName = "Daniel Moore";
        System.out.println("after theName: " + theName);
        System.out.println("after anotherName: " + anotherName);
        // interestingly the anotherName kept the same
        // it behaves like a primitive data type

        // another test with reference data types
        Person bob = new Person("Bob Peterson");
        Person alice = bob; // I think this passed by reference, not copy
        System.out.println("before bob: " + bob.name); // Bob Peterson
        System.out.println("before alice: " + alice.name); // Bob Peterson

        // change bob
        bob.name = "Harry Potter";

        System.out.println("after bob: " + bob.name); // Harry Potter
        System.out.println("after alice: " + alice.name); // Harry Potter
        // both variables changed


    }

    static class Person {
        String name;

        public Person(String name) {
            this.name = name;
        }
    }

}
// next video:
// https://youtu.be/Qgl81fPcLc8?t=4245