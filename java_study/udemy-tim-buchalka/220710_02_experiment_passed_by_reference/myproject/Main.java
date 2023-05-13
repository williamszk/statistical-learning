package myproject;

public class Main {

    public static void main(String[] args) {

        Animal doggy = new Animal("Doggy", 1);
        System.out.println("Calling from outside: \t\t\t\t" + doggy);
        handleAnimal(doggy);

        doggy.handleFromInside();
        // Calling from outside:                           myproject.Animal@372f7a8d
        // Calling from inside handleAnimal():             myproject.Animal@372f7a8d
        // Calling from inside handleFromInside():         myproject.Animal@372f7a8d
    }

    public static void handleAnimal(Animal animal) {
        System.out.println("Calling from inside handleAnimal(): \t\t" + animal);
    }
}

// Note that myShip2 is a reference to the instance of Ship
// In Java functions are methods passed by reference or by value?
// There is a difference between a method that is changing an
// object, and an object that is being used as an argument 

// In Go, when we use a method can we change its internal 
// properties too?
// or the object itself is passed as value?