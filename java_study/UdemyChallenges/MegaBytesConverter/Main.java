public class Main {
    // https://www.udemy.com/course/java-the-complete-java-developer-course/learn/quiz/4426604#overview
    public static void main(String[] args) {

        printMegaBytesAndKiloBytes(2500);
        printMegaBytesAndKiloBytes(-1024);
        printMegaBytesAndKiloBytes(5000);
    
    }

    public static void printMegaBytesAndKiloBytes(int kiloBytes) {
        String message = "Invalid Value";

        if (kiloBytes >= 0) {
            int megaBytes;
            int remainingKiloBytes;
    
            megaBytes = kiloBytes/1024;
            remainingKiloBytes = kiloBytes % 1024;

            message = kiloBytes + " KB = "+megaBytes+" MB and "+remainingKiloBytes+" KB";
        }
        System.out.println(message);
    }

}
