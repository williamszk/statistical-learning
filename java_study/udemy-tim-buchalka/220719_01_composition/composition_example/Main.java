package composition_example;

public class Main {
    public static void main(String[] args) {
        Dimensions dimensions = new Dimensions(20, 20, 5);
        Case theCase = new Case("220b", "Dell", "240", dimensions) ;

        Monitor theMonitor = new Monitor("27inch", "Acer", 27, new Resolution(2540, 1440));

        Motherboard theMontherBoard = new Motherboard("BJ-200", "Asus", 4,6, "v2.44");
        
        PersonalComputer thePC =  new PersonalComputer(theCase, theMonitor, theMontherBoard);

        // examples of composition
        // thePC.getMonitor().drawPixelAt(1500, 1200, "red");
        // thePC.getMotherboard().loadProgram("Windows 1.0");
        // thePC.getTheCase().pressPowerButton();
        thePC.powerUp();
    }
}

// to compile:
// C:\Users\william.suzuki\Documents\statistical-learning\java_study\220719_01_composition>javac composition_example\Main.java
// Note that we need to be one directory up
// to Run, in windows we need to take care to use / (forward slash) instead of backslash
// C:\Users\william.suzuki\Documents\statistical-learning\java_study\220719_01_composition>java composition_example/Main
// Drawing pixel at 1500, 1200 in color red
// Program Windows 1.0 is now loading.
// Power button pressed.