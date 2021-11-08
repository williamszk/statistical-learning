public class Main {
    public static void main(String[] args) {
        boolean output;
        output = toMilesPerHour(1.5) == 1;
        output = toMilesPerHour(10.25) == 6;
        output = toMilesPerHour(-5.6) == -1;
    }

    private static final double KILOMETERS_TO_HOURS = 1.609;

    public static long toMilesPerHour(double kilometerPerHour) {
        long output = -1;
        if (kilometerPerHour >= 0) {
            double milesPerHour = kilometerPerHour / KILOMETERS_TO_HOURS;
            output = Math.round(milesPerHour);
        }
        return output;
    }

    public static void printConversion(double kilometerPerHour) {
        String message = "Invalid Value";
        if (kilometerPerHour >= 0) {
            long milesPerHour = toMilesPerHour(kilometerPerHour);
            message = kilometerPerHour + " km/h = " + milesPerHour + " mi/h";
        }
        System.out.println(message);
    }

}
