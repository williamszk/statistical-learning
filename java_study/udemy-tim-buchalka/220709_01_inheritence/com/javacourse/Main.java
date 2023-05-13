package com.javacourse;

// https://www.udemy.com/course/java-the-complete-java-developer-course/learn/lecture/3133100#overview

public class Main {

    public static void main(String[] args) {

        System.out.println("Hello World!");

        Animal myAnimal = new Animal("Rat", 1, 1, 2, 3);
        myAnimal.eat();

        Dog myDog = new Dog("Doggy", 10, 9, 2, 4, 1, 1, "Furry");

        myDog.eat();

        myDog.walk();
    }
}
