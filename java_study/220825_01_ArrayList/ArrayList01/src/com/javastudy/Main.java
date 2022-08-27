package com.javastudy;

public class Main {
    public static void main(String[] args) {

        GroceryList myGroceryList =  new GroceryList();
        myGroceryList.addGroceryItem("Apples");
        myGroceryList.addGroceryItem("Oranges");
        myGroceryList.addGroceryItem("Butter");


        myGroceryList.printGroceryList();

        myGroceryList.modifyGroceryItem(1, "Tangerines");

        myGroceryList.removeGroceryItem(0);

        myGroceryList.findItem("Butter");

    }
}
