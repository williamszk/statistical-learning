
# Notes

The main aspect about having an abstract factory pattern with only functions
is that the abstract factory needs to return another function
The polygon package will be the same. That shows that the concrete implementation
should/does not care/know about the patterns around it for its creation.
Using FP or OOP approaches for abstract factories does not touch the
concrete implementation.
Even doing a simple factory pattern in this case wouldn't touch the
concrete implementations.

The FP abstract factory is a strange solution.
The OOP seems more natural to me at least.
With the OOP pattern I can control have more control.
For example instead of all 9 structs implementing a single Polygon
interface 3 implement only for blue specific interface and so on,
we could do this using OOP. For FP I'm not sure how to do it.

How should we implement the abstract factory pattern if the interfaces for
different shapes where different?
For example:
Triangles should have a method called TriangleType().
Rectangles should have a method called IsSquare().
Pentagon should have a method called isSymmetric().

We could have another situation where for each color the structs should do
something specific:
Red Polygons should have a method DoRedStuff.
Blue polygons should have a method DoBlueStuff.
Green polygons should have a method DoGreenStuff.

Even with those requirements about the structs we can build a single method called
"Get" which is specified in an interface which could be used for telling the
constructor which type it should output.

---

We could have built the top most factory layer as just a function.
And the lower ones as structs with methods.

---

Try to build the factory and abstract factory patterns using the struct
embedded in struct way. See if it is possible.
It is not possible embedding structs inside structs did not allow use to
tell that Triangle is a type of Polygon.
For Go this is not relevant given that for Go what is important is that
Triangle behaves like a Polygon.
That is, we needed to use interfaces.
Triangle and Rectangle belong to the group of Polygons.
But this is not important for Go. It would be relevant if both Triangle and
Rectangle have some common behavior.
And this common behavior would tell the parameter or return of a function
what this type can do.
We know that both Triangle and Rectangle belong to the same group, but for
functions this does not matter. Only if both elements have some common
behavior which the function will use.

This is Duck typing.
The important thing is that the object will behave in a certain way.
If this is true, we can group those objects that behave in this way.
And we'll say that they have a certain type.
This is the interface.

In Rust we could tell that both Triangle and Rectangle are structs that belong
to the Polygon Enum.
Or in Python we could say that Triangle and Rectangle inherit from the Polygon
class, this would make `isinstance` function tell that Triangle and Rectangle
both are Polygons.
In Go this does not matter. The only thing that matters is behavior.
This gives freedom for objects.
Also it makes loosely coupled.
But lacking structure, and control over it.
Sometimes we want to make object types tightly coupled so that we can transmit
the information that they should belong in the same group.
