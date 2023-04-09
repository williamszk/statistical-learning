package factory

import "abstractfactory/polygon"

// build 3 structs each with a method that returns the Polygon Interface
// also build 1 interface that capture all those three structs

type FactoryColorPolygon interface {
	Create(numSides int) polygon.Polygon
}

type FactoryColorPolygonBlue struct{}

func (f FactoryColorPolygonBlue) Create(numSides int) polygon.Polygon {
	if numSides == 3 {
		return polygon.BlueTriangle{}
	} else if numSides == 4 {
		return polygon.BlueRectangle{}
	} else if numSides == 5 {
		return polygon.BluePentagon{}
	} else {
		return nil
	}
}

type FactoryColorPolygonRed struct{}

func (f FactoryColorPolygonRed) Create(numSides int) polygon.Polygon {
	if numSides == 3 {
		return polygon.RedTriangle{}
	} else if numSides == 4 {
		return polygon.RedRectangle{}
	} else if numSides == 5 {
		return polygon.RedPentagon{}
	} else {
		return nil
	}
}

type FactoryColorPolygonGreen struct{}

func (f FactoryColorPolygonGreen) Create(numSides int) polygon.Polygon {
	if numSides == 3 {
		return polygon.GreenTriangle{}
	} else if numSides == 4 {
		return polygon.GreenRectangle{}
	} else if numSides == 5 {
		return polygon.GreenPentagon{}
	} else {
		return nil
	}
}
