
class Main {
    public static void main(String[] args) {
        // calling context
        HttpClient client = new HttpClient();
        App.start(client);
    }
}

class App {
    public static void start(ClientInterface client){
        client.getUser("bob@clean.com");
        User user = new User("Bob", "bob@clean.com");
        client.createUser(user);
    }
}

interface ClientInterface {
    public void getUser(String email);
    public void createUser(User user);
}

class HttpClient implements ClientInterface {

    public HttpClient(){
    }

    public void getUser(String email){
        System.out.println("Getting user... " + email);
    };

    public void createUser(User user){
        System.out.println("Creating user... " + user.name);
    };
}

class User{
    public String name;
    public String email;

    public User(String name, String email){
        this.name = name;
        this.email = email;
    }
}


