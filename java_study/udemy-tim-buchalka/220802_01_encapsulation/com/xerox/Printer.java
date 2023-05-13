package com.xerox;

public class Printer {

    private int tonerLevel;
    private int pagesPrinted;
    private boolean duplex;

    public Printer(int tonerLevel, boolean isDuplex) {
        if (tonerLevel > -1 && tonerLevel <= 100) {
            this.tonerLevel = tonerLevel;
        } else {
            this.tonerLevel = -1;
        }
        this.pagesPrinted = 0;
        this.duplex = isDuplex;
    }

    public int getTonerLevel() {
        return tonerLevel;
    }

    public int getPagesPrinted() {
        return pagesPrinted;
    }

    public boolean getIsDuplex() {
        return duplex;
    }

    public void fillUpToner(int amount) {
        if (tonerLevel + amount > 100) {
            System.out.println("Error: the amount will overfill the toner.");
        } else {
            tonerLevel += amount;
            System.out.println("Toner filled up to " + getTonerLevel() + "%");
        }
    }

    public void printPage() {
        pagesPrinted += 1;
        System.out.println("Page printed.");

    }

}
