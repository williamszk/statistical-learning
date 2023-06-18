package com.javastudy;

public class Main {
    public static void main(String[] args) {

        System.out.println("Start mobile phone app.");

        MobilePhone mobilePhone = new MobilePhone();

        Contact contactBob = new Contact("Bob", "101010");
        mobilePhone.store(contactBob);
    }

}
