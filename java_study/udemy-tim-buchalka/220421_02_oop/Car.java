
public class Car {
  // public is an access modifier
  // it controls if other programs can access this class or not

  // In Java "attributes" are called "fields"
  // we need to use access modifiers too
  // to use the private access modifier will hide external access to the
  // internal workings of the class
  // The objective of Encapsulation is to hide the internal workings of the class

  private int doors;
  private int wheels;
  private String model;
  private String engine;
  private String color;
  // in Java, we set the fields as private so that we follow the principle of
  // encapsulation

  public void setModel(String model) {
    // include a test to see if the passed model is valid
    String validModel = model.toLowerCase();
    // to compare strings we need equals
    if (validModel.equals("carrera") || validModel.equals("commodore")) {
      this.model = model; // "this" is like "self" in Python
    } else {
      this.model = "Unknown";
      // if the valid values are not used as input
    }
  }

  public String getModel() {
    return this.model;
  }

  // String is a class
  // int is a primitive data type

}
