package factory

// build a struct that has a method called "createFactory"
// this method returns the interface for the concrete factories

type AbstractFactoryPolygon struct{}

func (a AbstractFactoryPolygon) CreateFactory(color string) FactoryColorPolygon {
	if color == "blue" {
		return FactoryColorPolygonBlue{}
	} else if color == "red" {
		return FactoryColorPolygonRed{}
	} else if color == "green" {
		return FactoryColorPolygonGreen{}
	} else {
		return nil
	}
}
