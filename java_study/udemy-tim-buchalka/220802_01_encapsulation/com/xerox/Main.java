package com.xerox;

public class Main {
    public static void main(String[] args) {
       Printer printer = new Printer(80, true);

       printer.fillUpToner(10);
       printer.fillUpToner(20);

       printer.printPage();
       System.out.println("Number of pages printed "+printer.getPagesPrinted());
       printer.printPage();
       System.out.println("Number of pages printed "+printer.getPagesPrinted());
       printer.printPage();
       System.out.println("Number of pages printed "+printer.getPagesPrinted());
    }
}