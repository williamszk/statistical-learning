package factory

import "abstractfactory/polygon"

// build a struct that has a method called "createFactory"
// this method returns the interface for the concrete factories

func AbstractFactoryPolygon(color string) func(int) polygon.Polygon {
	if color == "blue" {
		return FactoryColorPolygonBlue
	} else if color == "red" {
		return FactoryColorPolygonRed
	} else if color == "green" {
		return FactoryColorPolygonGreen
	} else {
		return nil
	}
}
