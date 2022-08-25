package com.javastudy;

public class BaseHamburger {
    private String breadRoll;
    private boolean meat;
    private boolean lettuce;
    private boolean tomato;
    private boolean cheese;
    private boolean bacon;
    private String burgerName;
    private double basePrice;
    private double lettucePrice;
    private double tomatoPrice;
    private double cheesePrice;
    private double baconPrice;


    public BaseHamburger(){
        this("Basic Breadroll", true, true, true, true, true, "Basic Burger", 2.00, 0.50, 0.40, 1.0, 2.0);
    }


    public BaseHamburger(String breadRoll, boolean meat, boolean lettuce, boolean tomato, boolean cheese, boolean bacon, String burgerName, double basePrice, double lettucePrice, double tomatoPrice, double cheesePrice, double baconPrice) {
        this.breadRoll = breadRoll;
        this.meat = meat;
        this.lettuce = lettuce;
        this.tomato = tomato;
        this.cheese = cheese;
        this.bacon = bacon;
        this.burgerName = burgerName;
        this.basePrice = basePrice;
        this.lettucePrice = lettucePrice;
        this.tomatoPrice = tomatoPrice;
        this.cheesePrice = cheesePrice;
        this.baconPrice = baconPrice;
    }

    public double calculateTotalPrice() {
        double totalPrice = 0;
        if (this.lettuce)
            totalPrice += lettucePrice;
        if (this.tomato)
            totalPrice += tomatoPrice;
        if (this.cheese)
            totalPrice += cheesePrice;
        if (this.bacon)
            totalPrice += baconPrice;

        return totalPrice;
    }

    public void setBreadRoll(String breadRoll) {
        this.breadRoll = breadRoll;
    }

    public void setMeat(boolean meat) {
        this.meat = meat;
    }

    public void setLettuce(boolean lettuce) {
        this.lettuce = lettuce;
    }

    public void setTomato(boolean tomato) {
        this.tomato = tomato;
    }

    public void setCheese(boolean cheese) {
        this.cheese = cheese;
    }

    public void setBacon(boolean bacon) {
        this.bacon = bacon;
    }

    public void setBurgerName(String burgerName) {
        this.burgerName = burgerName;
    }

    public double getBasePrice() {
        return basePrice;
    }

    public double getLettucePrice() {
        return lettucePrice;
    }

    public double getTomatoPrice() {
        return tomatoPrice;
    }

    public double getCheesePrice() {
        return cheesePrice;
    }

    public double getBaconPrice() {
        return baconPrice;
    }

}
