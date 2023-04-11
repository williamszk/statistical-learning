package main

// The difference here is that we'll use another way of telling Go that
// Triangle is a type of Polygon
// I think we can call it the alias type

import "fmt"

func main() {
	fmt.Println("Hello World")
	fmt.Println("== From calling classes directly ====================================")

	tri := Triangle{}
	tri.get()

	rec := Rectangle{}
	rec.get()

	pen := Pentagon{}
	pen.get()

	fmt.Println("== From calling the factoryMethod ====================================")

	tri2 := FactoryPolygon{}.create(3)
	tri2.get()

	rec2 := FactoryPolygon{}.create(4)
	rec2.get()

	pen2 := FactoryPolygon{}.create(5)
	pen2.get()

}

type Triangle Polygon

func (t Triangle) get() {
	fmt.Println("Hello from a Triangle")
}

type Rectangle Polygon

func (r Rectangle) get() {
	fmt.Println("Hello from a Rectangle")
}

type Pentagon Polygon

func (p Pentagon) get() {
	fmt.Println("Hello from a Pentagon")
}

type Polygon struct{}

type FactoryPolygon struct{}

func (f FactoryPolygon) create(numSides int) Polygon {
	if numSides == 3 {
		return Triangle{}
	} else if numSides == 4 {
		return Rectangle{}
	} else if numSides == 5 {
		return Pentagon{}
	} else {
		return nil
	}
}

// This doesn't work neither
