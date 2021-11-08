public class Main {
    public static void main(String[] args){
        System.out.println("Hello there!");
        float myMinFloat = Float.MIN_VALUE;
        float myMaxFloat = Float.MAX_VALUE;
        System.out.println("myMinFloat = " + myMinFloat);
        System.out.println("myMaxFloat = " + myMaxFloat);

        double myMinDouble = Double.MIN_VALUE;
        double myMaxDouble = Double.MAX_VALUE;
        System.out.println("myMinDouble = " + myMinDouble);
        System.out.println("myMaxDouble = " + myMaxDouble);

        int myIntValue = 5 / 2;
        float myFloatValue = 5F / 3F;
        // double is the default value for floats in Java
        // as well as int is the default value for int
        double myDoubleValue = 5.0 / 3.0;

        System.out.println("myIntValue = " + myIntValue);
        System.out.println("myFloatValue = " + myFloatValue);
        System.out.println("myDoubleValue = " + myDoubleValue);

        // Challenge
        double POUND_TO_KILOGRAM = 0.45359237D;
        double KILOGRAM_TO_POUND = 1D / POUND_TO_KILOGRAM;

        double valuePounds = 90D;
        double valueKilograms = POUND_TO_KILOGRAM * valuePounds;

        System.out.println(valuePounds + " pounds is equal to " + valueKilograms + " kilograms.");

        double valuePounds2 = KILOGRAM_TO_POUND * valueKilograms;
        System.out.println(valueKilograms + " kilograms is equal to " + valuePounds2 + " pounds.");
    }
}
