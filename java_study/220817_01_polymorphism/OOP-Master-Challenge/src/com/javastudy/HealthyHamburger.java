package com.javastudy;

public class HealthyHamburger extends BaseHamburger {
    private boolean pickle;
    private boolean onion;
    private double onionPrice;
    private double picklePrice;

    public HealthyHamburger() {
        this(true, true, 1.00, 1.50);
    }


    public HealthyHamburger(boolean pickle, boolean onion, double onionPrice, double picklePrice) {
        this.pickle = pickle;
        this.onion = onion;
        this.onionPrice = onionPrice;
        this.picklePrice = picklePrice;
    }

    public void setPickle(boolean pickle) {
        this.pickle = pickle;
    }

    public void setOnion(boolean onion) {
        this.onion = onion;
    }

    public void setOnionPrice(double onionPrice) {
        this.onionPrice = onionPrice;
    }

    public void setPicklePrice(double picklePrice) {
        this.picklePrice = picklePrice;
    }
}
