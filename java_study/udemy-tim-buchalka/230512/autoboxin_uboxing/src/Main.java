import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        String[] strArray = new String[10];
        int[] intArray = new int[10];

        ArrayList<String> strArrayList = new ArrayList<String>();
        strArrayList.add("Bob");

        // this will give an error, because int is not a class it is a primitive type
        // ArrayList<int> intArrayList = new ArrayList<int>();
        ArrayList<IntClass> intClassArrayList = new ArrayList<IntClass>();
        intClassArrayList.add(new IntClass(10));

        Integer myInteger = new Integer(42);
        Double myDouble = new Double(1.98);

        ArrayList<Integer> myArrayListInteger = new ArrayList<Integer>();
        for (int i = 0; i < 10; i++) {
            // using Integer.valueOf(i) is called autoboxing
            myArrayListInteger.add(Integer.valueOf(i));
        }

        for (int i = 0; i < 10; i++) {
            // method intValue will convert Integer into primitive int
            // the method intValue is doing the unboxing
            System.out.println(i + " --> " + myArrayListInteger.get(i).intValue());
            // we call autoboxing and unboxing because its purpose is to create a box (class) in which
            // we can pass primitive types to some other container types.
        }

        // there is a syntactic sugar for autoboxing
        Integer myIntVal01 = 55;
        // we actually don't need to use `new Integer(55)`, Java will know we are using boxing here
        // or another way of creating is `Integer.valueOf(55)`

        // we can easily convert a boxed value by:
        int myIntVal02 = myIntVal01;
        // this is automatic unboxing
        // below is the extensive way of unboxing
        int myIntVal03 = myIntVal01.intValue();


        ArrayList<Double> myArrayListDouble = new ArrayList<Double>();
        for (double i = 0.0; i < 10.0; i += 0.3) {
            myArrayListDouble.add(i);
        }
        System.out.println("-------------------------------------------------------");
        for (int i = 0; i < myArrayListDouble.size(); i++) {
            double value = myArrayListDouble.get(i);
            System.out.println(i + " --> " + value);
        }

    }
}

class IntClass {
    private int value;

    public IntClass(int value) {
        this.value = value;
    }

    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
}