package main

import "fmt"

// Given a rectangle find the dimenions of the square such that we can
// perfectly fill the rectangle with squares

func main() {
	heightRectangle := 1680.0
	widthRectangle := 640.0

	squareLength := findSquareFillRectangle(heightRectangle, widthRectangle)
	fmt.Println("squareLength = ", squareLength)

	// squareLength2 := findSquareFillRectangle(1982.0, 1231.1)
	// fmt.Println("squareLength2 = ", squareLength2)
}

// Return the length of the side of the square. A square such that can fill
// the rectangle with dimensions passed to the function.
func findSquareFillRectangle(heightRectangle float64, widthRectangle float64) float64 {
	// we need to know the smaller side of the rectangle and use it to cut a
	// squre out of the rectangle, we'll then use the rectangle that was left
	// for the next run of the recursion, until we find the smalles square
	newHeight := 0.0
	newWidth := 0.0

	fmt.Printf("(height, width) = (%v, %v)\n", heightRectangle, widthRectangle)
	if widthRectangle == heightRectangle {
		// if both sides are the same, then it is a square, this is smalles
		// square which can fill the rectangle
		// we can return either side
		return widthRectangle
	} else if widthRectangle < heightRectangle {
		// the width is the smaller side
		// create the new rectangle
		newHeight = heightRectangle - widthRectangle
		newWidth = widthRectangle
	} else {
		// the height is the smaller side
		// create the new rectangle
		newHeight = heightRectangle
		newWidth = widthRectangle - heightRectangle
	}

	return findSquareFillRectangle(newHeight, newWidth)
}
