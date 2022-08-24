package com.javastudy;

import java.util.Scanner;

public class ConsoleView {

    private static final Scanner scanner = new Scanner(System.in);


    public void main(){
        System.out.println("---------------------------------------------------------------------------------------");
        System.out.println("#=====================================================#");
        System.out.println("# Welcome to the Bill's Burger Management Software!   #");
        System.out.println("#=====================================================#");
        startQueryForHamburger();
    }

    /**
     * This function is used for asking the cashier for the characteristics
     * of the hamburger, given the order of the client.
     *
     * */
    public void startQueryForHamburger(){

        while (true) {

            System.out.print("What is the desired type of burger?");
            System.out.println(" (write the number and then press Enter)");
            System.out.println("1. Basic Burger");
            System.out.println("2. Healthy Burger");
            System.out.println("3. Deluxe Burger");

            System.out.print("> ");
            int desiredTypeOfBurger = scanner.nextInt();

            // Maybe in here it would make more sense to use some kind of hashmap
            String message = "The desired burger is: ";
            switch (desiredTypeOfBurger){
                case 1:
                    message += "Basic Burger";
                    break;
                case 2:
                    message += "Healthy Burger";
                    break;
                case 3:
                    message += "Deluxe Burger";
                    break;
                default:
                    break;
            }
            if (desiredTypeOfBurger >= 1 && desiredTypeOfBurger <= 3){
                System.out.println(message);
                break;
            } else {
                System.out.println("Error... The typed value of " + desiredTypeOfBurger +
                        " is not recognized. Please, choose an available option:");
            }
        }
    }
    /**
     * This function prints the report for the chosen hamburger.
     *
     * This function is part of the View layer, so it should not contain any
     * functionality related to the domain logic layer.
     * It should only call the domain logic layer methods, and organize them
     * into a human-readable format.
     * */
    public void printReport(BaseHamburger hamburger){

    }
}
