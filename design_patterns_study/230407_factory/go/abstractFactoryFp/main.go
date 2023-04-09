// The main aspect about having an abstract factory pattern with only functions
// is that the abstract factory needs to return another function
// The polygon package will be the same. That shows that the concrete implementation
// should/does not care/know about the patterns around it for its creation.
// Using FP or OOP approaches for abstract factories does not touch the
// concrete implementation.
// Even doing a simple factory pattern in this case wouldn't touch the
// concrete implementations.

package main

import (
	"abstractfactory/factory"
	"abstractfactory/polygon"
	"fmt"
)

func main() {
	fmt.Println("Hello World")
	fmt.Println("== From calling classes directly ====================================")

	tri := polygon.BlueTriangle{}
	tri.Get()
	tri2 := polygon.RedTriangle{}
	tri2.Get()
	tri3 := polygon.GreenTriangle{}
	tri3.Get()

	rec := polygon.BlueRectangle{}
	rec.Get()
	rec2 := polygon.RedRectangle{}
	rec2.Get()
	rec3 := polygon.GreenRectangle{}
	rec3.Get()

	pen := polygon.BluePentagon{}
	pen.Get()
	pen2 := polygon.RedPentagon{}
	pen2.Get()
	pen3 := polygon.GreenPentagon{}
	pen3.Get()

	fmt.Println("== From calling the factoryMethod ====================================")

	factory.AbstractFactoryPolygon("blue")(3).Get()
	factory.AbstractFactoryPolygon("blue")(4).Get()
	factory.AbstractFactoryPolygon("blue")(5).Get()

	factory.AbstractFactoryPolygon("red")(3).Get()
	factory.AbstractFactoryPolygon("red")(4).Get()
	factory.AbstractFactoryPolygon("red")(5).Get()

	factory.AbstractFactoryPolygon("green")(3).Get()
	factory.AbstractFactoryPolygon("green")(4).Get()
	factory.AbstractFactoryPolygon("green")(5).Get()

	// This is a strange solution.
	// The OOP seems more natural to me at least.
	// With the OOP pattern I can control have more control.
	// For example instead of all 9 structs implementing a single Polygon
	// interface 3 implement only for blue specific interface and so on,
	// we could do this using OOP. For FP I'm not sure how to do it.
}
