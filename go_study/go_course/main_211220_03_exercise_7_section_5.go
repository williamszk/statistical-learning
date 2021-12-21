// https://www.youtube.com/watch?v=9eMbGsKcWlc&list=PLCKpcjBB_VlBsxJ9IseNxFllf-UFEXOdg&index=37&ab_channel=AprendaGo

package main

import "fmt"

func main() {

	var myBoolean bool

	fmt.Println(myBoolean)

	var myInt int
	fmt.Printf("%v, %T", myInt, myInt)

	myDecimal := 31337
	fmt.Printf("%d, %#x", myDecimal, myDecimal)

}
