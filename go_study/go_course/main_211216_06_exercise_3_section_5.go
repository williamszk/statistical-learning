// https://www.youtube.com/watch?v=12o81rTFu_w&list=PLCKpcjBB_VlBsxJ9IseNxFllf-UFEXOdg&index=33&ab_channel=AprendaGo
// crie constantes tipadas e não tipadas e demostre seus valores

package main

import "fmt"

// constants are not typed until they are needed

const myconst1 = 10
const myconst2 = 10

var myvar1 int
var myvar2 float64

func main() {

	myvar1 = myconst1
	fmt.Printf("%v, %T\n", myconst1, myconst1)

	// we can pass myconst2 to myvar2 because the constant
	// doesn't assume any type util it is needed
	// but interestingly we see that myconst2 is of type integer
	// when we pass it on the printf below...
	myvar2 = myconst2
	fmt.Printf("%v, %T\n", myconst2, myconst2)

}
