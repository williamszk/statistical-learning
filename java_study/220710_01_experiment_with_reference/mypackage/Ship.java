package mypackage;

public class Ship {
    private int size;
    private String purpose;

    public Ship(int size, String purpose) {
        this.size = size;
        this.purpose = purpose;
    }

    public void move() {
        System.out.println("Move the ship");
    }

    public void setSize(int size) {
        this.size = size;
    }

    public void setPurpose(String purpose) {
        this.purpose = purpose;
    }

    public int getSize() {
        return this.size;
    }

    public String getPurpose() {
        return this.purpose;
    }
}