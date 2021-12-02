package main

import "fmt"

// write a function slope where we pass as arguments 2 coordinates
// x1, y1, x2, y2
// slope returns the slope between the two points
// then write a function intercept that returns the intercept
// we need to use the function slope inside intercept

func main() {

	xOne := 1.0
	yOne := 9.0

	xTwo := 2.0
	yTwo := 2.0

	fmt.Println("coordinate one:", xOne, yOne)
	fmt.Println("coordinate two:", xTwo, yTwo)

	slope := FindSlope(xOne, yOne, xTwo, yTwo)

	fmt.Println("slope =", slope)

	intercept := FindIntercept(xOne, yOne, xTwo, yTwo)

	fmt.Println("intercept =", intercept)

}

func FindSlope(xOne float64, yOne float64, xTwo float64, yTwo float64) float64 {
	return (yTwo - yOne) / (xTwo - xOne)
}

func FindIntercept(xOne float64, yOne float64, xTwo float64, yTwo float64) float64 {
	slope := FindSlope(xOne, yOne, xTwo, yTwo)
	return yTwo - slope*xTwo
}
