package imperative;

// If we want to run this class in the terminal
// we should compile from the root directory
// javac imperative/Main.java
// java imperative/Main
// I tried running from the imperative directory 
// and it didn't work

import java.util.ArrayList;
import java.util.List;
import java.util.function.Predicate;
import java.util.stream.Collectors;

/**
 * Main
 */
public class Main {
    public static void main(String[] args) {
        // create a list of people
        // List is a class
        // Person is a class that is inside the List

        List<Person> people = List.of(
                new Person("John", Gender.MALE),
                new Person("Maria", Gender.FEMALE),
                new Person("Aisha", Gender.FEMALE),
                new Person("Alex", Gender.MALE),
                new Person("Alice", Gender.FEMALE));

        // find out how many females that are there in the list
        // Imperative approach
        List<Person> females = new ArrayList<>();

        for (Person person : people) {
            if (Gender.FEMALE.equals(person.gender)) {
                females.add(person);
                // .add must be like push, or append for an ArrayList

            }
        }

        // print all people inside the ArrayList of females
        for (Person person : females) {
            System.out.println(person);
        }

        System.out.println("\nFunctional way of printing all people");
        people.forEach(System.out::println);

        System.out.println("\nFunctional Approach");
        // Declarative Approach
        // Functional Approach
        people.stream()
                .filter(person -> Gender.FEMALE.equals(person.gender))
                .forEach(System.out::println);

        List<Person> females2 = people.stream()
                .filter(person -> Gender.FEMALE.equals(person.gender))
                .collect(Collectors.toList());

        System.out.println("\nFunctional Approach another way");
        females2.forEach(System.out::println);

        // this way reminds me a javascript.
        // how would this fit with Clojure?
        // this way makes heavy use of chainning, which needs to be based
        // on OOP because it uses methods on objects, but at the same time it 
        // is functional..., this is trange
        // could we say that in Clojure we can also have channing?
        // I don't think so.
        //

        // example working Predicate

        // the predicate works like an arrow function, but it needs to return
        // a boolean
        Predicate<Person> personPredicate = person -> Gender.FEMALE.equals(person.gender);

        List<Person> females3 = people.stream()
                .filter(personPredicate)
                .collect(Collectors.toList());

        System.out.println("\nFunctional Approach using Predicate");
        females3.forEach(System.out::println);
    }

    static class Person {
        // the final keyword is used to make it a const
        private final String name;
        private final Gender gender;

        // now we need to build a constructor
        // ideally in a Java IDE we should have code generators
        // for building constructors
        Person(String name, Gender gender) {
            this.name = name;
            this.gender = gender;
        }

        @Override
        public String toString() {
            return "Person{" +
                    "name='" + name + '\'' +
                    ", gender=" + gender +
                    '}';
        }
    }

    // define a gender
    enum Gender {
        MALE, FEMALE
    }
}
