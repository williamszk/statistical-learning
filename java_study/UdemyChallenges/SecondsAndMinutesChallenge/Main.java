
public class Main {

    public static void main(String[] args) {
        String message1 = getDurationString(10, 40);
        String message1a = getDurationString(987, 8);
        String message2 = getDurationString(800);
        String message3 = getDurationString(-109);
    }

    // final makes the variable unchangeble
    private static final String INVALID_VALUE_MESSAGE = "Invalid Value";

    public static String includeLeadingZero(int number) {
        String output =  String.valueOf(number);
        if (number < 10) {
            output = "0" + number;
        }
        return output;
    }

    public static String getDurationString(int minutes, int seconds) {
        String message = INVALID_VALUE_MESSAGE;
        if (minutes >= 0 && seconds >= 0 && seconds <= 59) {
            int hours = minutes/60;
            int minutesRemainder = minutes % 60;
            String hoursString = includeLeadingZero(hours);
            String minutesString = includeLeadingZero(minutesRemainder);
            String secondsString = includeLeadingZero(seconds);
            message = hoursString + "h " + minutesString + "m " + secondsString + "s";
        }
        return message;
    }

    public static String getDurationString(int seconds) {
        String message = INVALID_VALUE_MESSAGE;
        if (seconds >= 0) {
            int minutes = seconds / 60;
            int secondsRemainder = seconds % 60;
            message = getDurationString(minutes, secondsRemainder);
        }
        return message;
    }

}