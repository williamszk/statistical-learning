package myproject;

public class Animal {

    private String name;
    private int size;
    
    public Animal(String name, int size) {
        this.name = name;
        this.size = size;
    }

    public String getName() {
        return this.name;
    }

    public int getSize() {
        return this.size;
    }

    public void handleFromInside(){
        System.out.println("Calling from inside handleFromInside(): \t" + this);
    }

}
