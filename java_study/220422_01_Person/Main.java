public class Main {
    public static void main(String[] args) {
        // https://www.udemy.com/course/java-the-complete-java-developer-course/learn/quiz/4585938#overview

        Person person = new Person();

        person.setFirstName("");
        person.setLastName("");
        person.setAge(10);

        System.out.println("fullName = " + person.getFullName());
        System.out.println("teen = " + person.isTeen());

        person.setFirstName("John");
        person.setAge(18);

        System.out.println("fullName = " + person.getFullName());
        System.out.println("teen = " + person.isTeen());

        person.setLastName("Smith");
        System.out.println("fullName = " + person.getFullName());
    }
}
