public class Main {
  // https://www.udemy.com/course/java-the-complete-java-developer-course/learn/lecture/3133062#overview
  // https://www.udemy.com/course/java-the-complete-java-developer-course/learn/lecture/3133104#overview
  public static void main(String[] args) {
    Car porsche = new Car();
    Car holdem = new Car();

    // print before we set any value to the instance
    // it will return null
    System.out.println("The model: " + porsche.getModel());
    porsche.setModel("Carrera");
    System.out.println("The model: " + porsche.getModel());

    porsche.setModel("Gol");
    System.out.println("The model: " + porsche.getModel());
  }
}
