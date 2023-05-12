import javax.print.attribute.SupportedValuesAttribute;

public class Main {
    public static void main(String[] args) {

        BankAccount bobBankAccount = new BankAccount();

        bobBankAccount.setAccountNumber(12345);

        bobBankAccount.setBalance(10000.00);

        bobBankAccount.setCustomerName("Bob Martin");

        bobBankAccount.setEmail("bob@martin.com");

        bobBankAccount.setPhoneNumber("1111-1111");

        System.out.println("Bank Account information: ");

        System.out.println("Account Number: " + bobBankAccount.getAccountNumber());

        System.out.println("Balance: " + bobBankAccount.getBalance());

        System.out.println("Customer Name: " + bobBankAccount.getCustomerName());

        System.out.println("Email: " + bobBankAccount.getEmail());

        System.out.println("Phone Number: " + bobBankAccount.getPhoneNumber());

        System.out.println("Event of Deposit funds");

        bobBankAccount.depositFunds(5000.00);

        System.out.println("Balance: " + bobBankAccount.getBalance());

        System.out.println("Event of withdraw funds above the available.");

        bobBankAccount.withdrawFunds(20000.00);

        System.out.println("Event of try another withdraw fund operations.");

        bobBankAccount.withdrawFunds(200.00);

        System.out.println("Balance: " + bobBankAccount.getBalance());

        BankAccount aliceBankAccount = new BankAccount(123454, 200000.00, "Alice",
                "alice@bank.com", "0000-1111");

        System.out.println("\nBank Account information: ");
        System.out.println("Account Number: " + aliceBankAccount.getAccountNumber());
        System.out.println("Balance: " + aliceBankAccount.getBalance());
        System.out.println("Customer Name: " + aliceBankAccount.getCustomerName());
        System.out.println("Email: " + aliceBankAccount.getEmail());
        System.out.println("Phone Number: " + aliceBankAccount.getPhoneNumber());

        BankAccount defaultBankAccount = new BankAccount();

        System.out.println("\nA test with default constructor, Bank Account information: ");
        System.out.println("Account Number: " + defaultBankAccount.getAccountNumber());
        System.out.println("Balance: " + defaultBankAccount.getBalance());
        System.out.println("Customer Name: " + defaultBankAccount.getCustomerName());
        System.out.println("Email: " + defaultBankAccount.getEmail());
        System.out.println("Phone Number: " + defaultBankAccount.getPhoneNumber());

    }

}
