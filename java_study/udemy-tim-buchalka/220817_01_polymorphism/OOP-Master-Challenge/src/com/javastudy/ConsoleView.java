package com.javastudy;

import java.util.Scanner;

public class ConsoleView {

    private static final Scanner scanner = new Scanner(System.in);

    private static String fixedLengthString(String string, int length) {
        // https://stackoverflow.com/a/13475390/8782077
//        return String.format( "%1$"+length+ "s", string );
        // we need to include $- with a minus to make if add padding to the right
        return String.format("%1$-" + length + "s", string);
    }

    public void main() {
        System.out.println("---------------------------------------------------------------------------------------");
        System.out.println("#=====================================================#");
        System.out.println("# Welcome to the Bill's Burger Management Software!   #");
        System.out.println("#=====================================================#");
        startQueryForHamburger();
    }

    public BaseHamburger instantiateHamburger() {
        while (true) {
            System.out.print("What is the desired type of burger?");
            System.out.println(" (write the number and then press Enter)");
            System.out.println("1. Basic Burger");
            System.out.println("2. Healthy Burger");
            System.out.println("3. Deluxe Burger");

            System.out.print("> ");
            int desiredTypeOfBurger = scanner.nextInt();
            // one problem that can arise in this case is that
            // if we type for example "5]" there will be a runtime exception
            // that maybe we should catch

            // Maybe in here it would make more sense to use some kind of hashmap
            String message = "The desired burger is: ";
            switch (desiredTypeOfBurger) {
                case 1:
                    return new BaseHamburger();
                case 2:
                    return new HealthyHamburger();
                case 3:
                    return new DeluxeHamburger();
                default:
                    System.out.println("Error... The typed value of " + desiredTypeOfBurger +
                            " is not recognized. Please, choose an available option:\n");
                    break;
            }
        }
    }

    private void showMessageForChosenHamburger(BaseHamburger hamburger) {
        System.out.println("The chosen hamburger is: " + hamburger.getClass().getSimpleName() + ".\n");
    }

    /**
     * This function is used for asking the cashier for the characteristics
     * of the hamburger, given the order of the client.
     */
    public void startQueryForHamburger() {

        BaseHamburger hamburger = instantiateHamburger();
        showMessageForChosenHamburger(hamburger);
        queryAdditions(hamburger);
        printReport(hamburger);


        // In here we should include an option to change the chosen items in the Hamburger

        // I need to include an inquiry session about the optional additions
        // on the burgers:
        // Only the Deluxe Does not have the options of exclusion of additions

        // we should include another functionality for checking if the chosen options
        // are correct

    }

    private void setPropertyOfHamburger(BaseHamburger hamburger, String additionName, boolean option) {
        switch (additionName) {
            case "Lettuce":
                hamburger.setLettuce(option);
                break;
            case "Tomato":
                hamburger.setTomato(option);
                break;
            case "Cheese":
                hamburger.setCheese(option);
                break;
            case "Bacon":
                hamburger.setBacon(option);
                break;
        }
    }

    private double getAdditionPriceGivenName(BaseHamburger hamburger, String additionName) {
        switch (additionName) {
            case "Lettuce":
                return hamburger.getLettucePrice();
            case "Tomato":
                return hamburger.getTomatoPrice();
            case "Cheese":
                return hamburger.getCheesePrice();
            case "Bacon":
                return hamburger.getBaconPrice();
        }
        // the price returned should be -1, if the additionName is not found
        return -1.0;
    }

    private void queryOption(BaseHamburger hamburger, String additionName) {

        int answer;
        boolean askQuery = true;
//        System.out.println("Chose your type of Bread Roll");
        // list here the types of Bread Roll that we have

        while (askQuery) {
            System.out.println("Do we include " + additionName + "?   " + "($"+ String.format("%1$"+3+".2f", getAdditionPriceGivenName(hamburger, additionName)) +")");
            System.out.println("1. Yes");
            System.out.println("2. No");
            System.out.print("> ");
            answer = scanner.nextInt();
            switch (answer) {
                case 1:
                    setPropertyOfHamburger(hamburger, additionName, true);
                    askQuery = false;
                    break;
                case 2:
                    setPropertyOfHamburger(hamburger, additionName, false);
                    askQuery = false;
                    break;
                default:
                    System.out.println("Choose either the number 1 (for Yes) or number 2 (for No)");
                    askQuery = true;
                    break;
            }
        }
    }

    private void queryAdditions(BaseHamburger hamburger) {

        queryOption(hamburger, "Lettuce");
        queryOption(hamburger, "Tomato");
        queryOption(hamburger, "Cheese");
        queryOption(hamburger, "Bacon");

//        if ("BaseHamburger".equals(hamburger.getClass().getSimpleName())) {
//        }
    }

    /**
     * This function prints the report for the chosen hamburger.
     * <p>
     * This function is part of the View layer, so it should not contain any
     * functionality related to the domain logic layer.
     * It should only call the domain logic layer methods, and organize them
     * into a human-readable format.
     */
    public void printReport(BaseHamburger hamburger) {


//        return String.format("%1$-" + length + "s", string);
        double totalPrice = 0.0;
        String borderBar = "+------------------------------------------------------------+";
        int lengthBar = borderBar.length() - 2;
        System.out.println(borderBar);
        printLineReport("      >>>>> Receipt Report  <<<<<", lengthBar);
        printLineReport("    Hamburger Type: " + hamburger.getBurgerName(), lengthBar);
        printLineReport("                    Base Price: " + " ... $" + String.format("%1$"+4+".2f", hamburger.getBasePrice()) , lengthBar);
        totalPrice += hamburger.getBasePrice();
        if (hamburger.isLettuce()) {
            totalPrice += hamburger.getLettucePrice();
            printLineReport("            Lettuce Additional: " + " ... $" + String.format("%1$"+4+".2f", hamburger.getLettucePrice()) , lengthBar);
        }
        if (hamburger.isTomato()) {
            totalPrice += hamburger.getTomatoPrice();
            printLineReport("             Tomato Additional: " + " ... $" +  String.format("%1$"+4+".2f", hamburger.getTomatoPrice()) , lengthBar);
        }
        if (hamburger.isCheese()) {
            totalPrice += hamburger.getCheesePrice();
            printLineReport("             Cheese Additional: " + " ... $" + String.format("%1$"+4+".2f", hamburger.getCheesePrice()) , lengthBar);
        }
        if (hamburger.isBacon()) {
            totalPrice += hamburger.getCheesePrice();
            printLineReport("              Bacon Additional: " + " ... $" + String.format("%1$"+4+".2f", hamburger.getBaconPrice()) , lengthBar);
        }
        printLineReport("                   Total Price: " + " ... $" + String.format("%1$"+4+".2f", totalPrice), lengthBar);


        System.out.println(borderBar);

    }

    private void printLineReport(String string, int baseLength) {
        String textContent = fixedLengthString(string, baseLength);
        System.out.println("|" + textContent + "|");
    }

}
