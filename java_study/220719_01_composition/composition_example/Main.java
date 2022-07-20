package composition_example;

public class Main {
    public static void main(String[] args) {
        Dimensions dimensions = new Dimensions(20, 20, 5);
        Case theCase = new Case("220b", "Dell", "240", dimensions) ;

        Monitor theMonitor = new Monitor("27inch", "Acer", 27, new Resolution(2540, 1440));

        Motherboard theMontherBoard = new Motherboard("BJ-200", "Asus", 4,6, "v2.44");
        
        PersonalComputer thePC =  new PersonalComputer(theCase, theMonitor, theMontherBoard);

        // examples of composition
        thePC.getMonitor().drawPixelAt(1500, 1200, "red");
        thePC.getMotherboard().loadProgram("Windows 1.0");
        thePC.getTheCase().pressPowerButton();
    }
}