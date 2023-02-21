
// This is the main class
class Application {
    ServiceFactory serviceFactory = ServiceFactory();
    Service service = serviceFactory.makeSvc();
}

// A concrete class
class ServiceFactory {
    Service makeSvc(){
    }
}

interface Service {
}

class ConcreteService implements Service {
}