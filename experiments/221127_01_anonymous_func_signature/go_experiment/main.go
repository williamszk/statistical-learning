package main

import "fmt"

func main() {

	// we have 4 parameters
	aClosureParam := 1111
	fooBar := "fooBar"
	spam := true
	eggs := 10.9

	chunkyBacon(aClosureParam, fooBar, spam, eggs)

	// using anonymous function
	// or immediately invoked function
	func() {
		fmt.Println("from anonymous:", aClosureParam, fooBar, spam, eggs)
	}()
	// this works!
	// note that we did not had to pass the parameters

}

func chunkyBacon(param int, fooBar string, spam bool, eggs float64) {
	fmt.Println("from function: ", param, fooBar, spam, eggs)
}
