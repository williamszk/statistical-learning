package com.javastudy;

public class BaseHamburguer {
    private String breadRoll;
    private boolean meat;
    private boolean lettuce;
    private boolean tomato;
    private boolean cheese;
    private boolean bacon;


    private String burguerName;


    private double basePrice;
    private double lettucePrice = 0.50;
    private double tomatoPrice = 0.43;
    private double cheesePrice = 1.12;
    private double baconPrice = 1.12;


    public BaseHamburguer(String breadRoll, boolean meat) {
        this.breadRoll = breadRoll;
        this.meat = meat;

        this.burguerName = "Basic Hamburguer";
        this.lettuce = true;
        this.tomato = true;
        this.cheese = true;
        this.bacon = true;
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
}
