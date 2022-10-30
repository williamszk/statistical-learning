package com.company;

public class AwesomeJavaProgram {

    public static void main(String[] args) {

        // TODO
        // FIXME
        int myInt = 7;

        System.out.println("myInt: " + myInt);

        double shoeSize = 9.5;

        double result = myInt * shoeSize;
        char myInitial = 'J';

        String myName = "John";

        myName.length();

        burp();

        printName("William");

        System.out.println(declareName("Bob"));


        if (true) {

        } else if (false) {

        } else {

        }

        for (int i = 0; i < 10; i++) {
            System.out.println(i);
        }

        Cat.dingDong();

        Cat myCat = new Cat();

        myCat.name = "Fred";
        myCat.age = 6;

        Cat anotherCat = new Cat();
        anotherCat.name = "Stella";
        anotherCat.age = 5;

    }

    private static void burp() {
        System.out.println("buurrrp");
    }

    private static void printName(String name) {
        System.out.println("My name is " + name);
    }

    private static String declareName(String name) {
        return "My name is " + name;
    }
}
