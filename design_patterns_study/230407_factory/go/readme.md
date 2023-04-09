
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