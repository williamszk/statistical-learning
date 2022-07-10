package mypackage;

public class Main {
    public static void main(String[] args) {

        Ship myShip = new Ship(100, "Transport");

        myShip.move();

        System.out.println(System.identityHashCode(myShip));
        System.out.println(myShip);

        Ship myShip2 = myShip;
        System.out.println(myShip2);

        System.out.println("Before: " + myShip.getPurpose());

        myShip2.setPurpose("Military");

        System.out.println("After: " + myShip.getPurpose());
    }
}

// Note that myShip2 is a reference to the instance of Ship
// In Java functions are methods passed by reference or by value?
// There is a difference between a method that is changing an
// object, and an object that is being used as an argument 

// In Go, when we use a method can we change its internal 
// properties too?
// or the object itself is passed as value?