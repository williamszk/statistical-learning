public class VipCustomer {
    private String customerName;
    private double creditLimit;
    private String customerEmailAddress;

    public VipCustomer() {
        this("Default Vip Customer Name", 100000.00, "default email address");
    }

    public VipCustomer(String customerName, double creditLimit, String customerEmailAddress) {
        this.customerName = customerName;
        this.creditLimit = creditLimit;
        this.customerEmailAddress = customerEmailAddress;
    }

    public void setCustomerName(String customerName) {
        this.customerName = customerName;
    }

    public void setCreditLimit(double creditLimit) {
        this.creditLimit = creditLimit;
    }

    public void setCustomerEmailAddress(String customerEmailAddress) {
        this.customerEmailAddress = customerEmailAddress;
    }

    public String getCustomerName() {
        return this.customerName;
    }

    public double getCreditLimit() {
        return this.creditLimit;
    }

    public String getCustomerEmailAddress() {
        return this.customerEmailAddress;
    }
}
