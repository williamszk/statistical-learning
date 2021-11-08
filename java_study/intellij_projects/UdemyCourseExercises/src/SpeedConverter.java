public class SpeedConverter {

    public static void main(String[] args) {

        boolean answer = toMilesPerHour(1.5) == 1;
        System.out.println(answer);

        answer = toMilesPerHour(10.25) == 6;
        System.out.println(answer);

        answer = toMilesPerHour(-5.6) == -1;
        System.out.println(answer);

        answer = toMilesPerHour(25.42) == 16;
        System.out.println(answer);

        answer = toMilesPerHour(75.114) == 47;
        System.out.println(answer);
    }

    public static long toMilesPerHour(double kilometersPerHour) {
        long output = -1;
        if (kilometersPerHour >= 0) {
            output = Math.round(kilometersPerHour/1.609);
        }
        return output;
    }

    public static void printConversion(double kilometersPerHour) {
        long milesPerHour = toMilesPerHour(kilometersPerHour);
        if (milesPerHour == -1) {
            System.out.println("Invalid Value");
        } else {
            System.out.println(kilometersPerHour + " km/h = " + milesPerHour + " mi/h");
        }
    }
}
