
class Application {
    ServiceFactory serviceFactory = ServiceFactory()
    Service service = serviceFactory.makeSvc()
}

interface Service {
}

class ConcreteImpl implements Service {
}

interface ServiceFactory {
    Service makeSvc(){}
}

class ServiceFactorImpl implements ServiceFactory {
    ConcreteImpl makeSvc(){
        return ConcreteImpl();
    }
}
