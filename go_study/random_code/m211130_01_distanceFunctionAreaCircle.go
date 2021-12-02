package main

// make a function that will find the distance between two points

import (
	"fmt"
	"math"
)

// what is the syntax convention in Go?
// https://betterprogramming.pub/naming-conventions-in-go-short-but-descriptive-1fa7c6d2f32a#:~:text=The%20convention%20in%20Go%20is,can%20safely%20stick%20to%20mixedCaps%20.
// pacakges should have just one word and be lower case, much like in python
// For functions that can be called outside we use the Pascal Case (MixedCaps)
// but if the function is to be used just internally we use camelCase.

func Distance(xFirst float64, yFirst float64, xSecond float64, ySecond float64) float64 {
	return math.Pow(math.Pow(xSecond-xFirst, 2)+math.Pow(ySecond-yFirst, 2), 0.5)
}

// how to use power in go?
// https://golangbyexample.com/power-golang/

// how to give variable names in go?
// https://medium.com/@lynzt/variable-naming-conventions-in-go-89fe1ef17b0a

// build a function for finding the area of a circle
// given the radius

func AreaCircle(radius float64) float64 {
	// how to get pi in go?
	// https://golangbyexample.com/pi-value-golang/

	return math.Pi * math.Pow(radius, 2)
}

func main() {

	xCenter := 0.0
	yCenter := 0.0

	fmt.Println("xCenter =", xCenter)
	fmt.Println("yCenter =", yCenter)

	// variable names should be camelCase
	// prefer to use abbreviations when those
	// do not interfere with interpretability
	xPnt := 1.0
	yPnt := 1.0

	fmt.Println("xPnt =", xPnt)
	fmt.Println("yPnt =", yPnt)

	dist := Distance(xCenter, yCenter, xPnt, yPnt)

	fmt.Println("dist =", dist)

	areaCircle := AreaCircle(dist)

	fmt.Println("areaCircle =", areaCircle)

}

// what is the difference between modules and namespaces?
