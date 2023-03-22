
This directory contains code inspired by the following problem:

We have a Duck class.
This class should have subclasses, which are specific types of ducks:
RedheadDuck, MallardDuck

The non-smart way is to make RedheadDuck and MallardDuck inherit from the 
Duck class.

There are other types of ducks.
DecoyDuck
RubberDuck

The DecoyDuck doesn't quack.
And the RubberDuck doesn't fly.

The naive way is to implement in the Duck (parent class) the methods for
fly() and quack()
The problem with this approach is that we'll give the same functionality to all
subclasses. But the DecoyDuck and RubberDuck do not both quack and fly.

One possible solution is to use an interface.

We create two new abstract classes:
QuackBehavior and FlyBehavior.

Then we need to implement concrete classes, which inherit from the abstract classes
of QuackBehavior and FlyBehavior. In the case of Java, there is a distinction
between interface and superclass. In the case of Python an interface is a superclass
with some decorators.

This example was taken from the Head First Design Patterns.

