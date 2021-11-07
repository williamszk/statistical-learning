public class Main {

    public static double INCHES_TO_CENTIMETERS = 2.54;

    public static void main(String[] args) {
        double centimetersCalculated1 = calcFeetAndInchesToCentimeters(2, 10);
        double centimetersCalculated2 = calcFeetAndInchesToCentimeters(34);
        double centimetersCalculated3 = calcFeetAndInchesToCentimeters(-2, 10);
        double centimetersCalculated4 = calcFeetAndInchesToCentimeters(10, 14);
    }

    public static double calcFeetAndInchesToCentimeters(int feet, int inches) {
        double output = -1;

        if (feet >= 0 && inches >= 0 && inches <= 12) {
            output = (inches + feet*12)*INCHES_TO_CENTIMETERS;
        }
        return output;
    }

    public static double calcFeetAndInchesToCentimeters(int inches) {
        double output = -1;

        if (inches >= 0) {
            output = inches*INCHES_TO_CENTIMETERS;
        }

        return output;
    }

}