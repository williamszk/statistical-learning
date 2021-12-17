// https://www.youtube.com/watch?v=Yaw80pKukMc&list=PLCKpcjBB_VlBsxJ9IseNxFllf-UFEXOdg&index=28&ab_channel=AprendaGo
// Constants
package main

import "fmt"

// we can declare many constants at the same time
const (
	x = 10
	y = 20
	z = 30
)

// can we do the same with var?

func main() {

	const myConstant = 10
	// const are lazy evaluated, until the myConst is not used, the program will not define its type
	fmt.Printf("%v, %T\n", myConstant, myConstant)

	fmt.Println(x, y, z)

}
