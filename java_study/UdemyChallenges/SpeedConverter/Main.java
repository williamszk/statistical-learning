public class Main {
    public static void main(String[] args) {

        testMethodToMilesPerHour(1.5, 1);
        testMethodToMilesPerHour(10.25, 6);
        testMethodToMilesPerHour(-5.6, -1);
        testMethodToMilesPerHour(25.42, 16);
        testMethodToMilesPerHour(75.114, 47);

    }

    public static void testMethodToMilesPerHour(double kilometersPerHour, long expectedMilesPerHour) {
        // This function is used for testing another method:
        // toMilesPerHour()
        // Examples:
        // testMethodToMilesPerHour(1.5, 1);
        // output:
        // true
        boolean resultTest = false;
        resultTest = toMilesPerHour(kilometersPerHour) == expectedMilesPerHour;
        System.out.println(resultTest);
    }

    public static long toMilesPerHour(double kilometersPerHour) {
        long milesPerHour = -1;

        if (kilometersPerHour >= 0) {
            double milesPerHourDouble = kilometersPerHour/1.609;
            milesPerHour = Math.round(milesPerHourDouble);
        }

        return milesPerHour;
    }

    public static void printConversion(double kilometersPerHour) {

        long milesPerHour = toMilesPerHour(kilometersPerHour);

        if (milesPerHour == -1) {
            System.out.println("Invalid Value");
        } else {
            System.out.println( kilometersPerHour + " km/h = " + milesPerHour + " mi/h");
        }
    }
}