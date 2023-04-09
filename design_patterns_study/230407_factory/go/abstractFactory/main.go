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

	factory.AbstractFactoryPolygon{}.CreateFactory("blue").Create(3).Get()
	factory.AbstractFactoryPolygon{}.CreateFactory("blue").Create(4).Get()
	factory.AbstractFactoryPolygon{}.CreateFactory("blue").Create(5).Get()

	factory.AbstractFactoryPolygon{}.CreateFactory("red").Create(3).Get()
	factory.AbstractFactoryPolygon{}.CreateFactory("red").Create(4).Get()
	factory.AbstractFactoryPolygon{}.CreateFactory("red").Create(5).Get()

	factory.AbstractFactoryPolygon{}.CreateFactory("green").Create(3).Get()
	factory.AbstractFactoryPolygon{}.CreateFactory("green").Create(4).Get()
	factory.AbstractFactoryPolygon{}.CreateFactory("green").Create(5).Get()

}
