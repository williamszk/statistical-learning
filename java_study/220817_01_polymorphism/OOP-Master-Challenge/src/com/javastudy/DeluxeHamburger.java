package com.javastudy;

public class DeluxeHamburger extends BaseHamburger {
    private boolean frenchFries;
    private boolean coke;
    private double frenchFriesPrice;
    private double cokePrice;

    public DeluxeHamburger(){
        this(true, true, 3.00, 2.00);
    }

    public DeluxeHamburger(boolean frenchFries, boolean coke, double frenchFriesPrice, double cokePrice) {
        this.frenchFries = frenchFries;
        this.coke = coke;
        this.frenchFriesPrice = frenchFriesPrice;
        this.cokePrice = cokePrice;
    }

    public void setFrenchFries(boolean frenchFries) {
        this.frenchFries = frenchFries;
    }

    public void setCoke(boolean coke) {
        this.coke = coke;
    }

    public void setFrenchFriesPrice(double frenchFriesPrice) {
        this.frenchFriesPrice = frenchFriesPrice;
    }

    public void setCokePrice(double cokePrice) {
        this.cokePrice = cokePrice;
    }
}
