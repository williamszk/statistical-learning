// https://www.youtube.com/watch?v=1IduyaGMO3g&list=PLCKpcjBB_VlBsxJ9IseNxFllf-UFEXOdg&index=29&ab_channel=AprendaGo

package main

import "fmt"

const (
	// why do we use iota?
	// when we don't care about the value of the constant
	// but we need some constant integer
	a = iota
	b = iota
	c = iota
	x = iota
	y = iota
	z = iota
)

// this will print succesive values of integers 0, 1, 2

func main() {
	fmt.Println(a, b, c)
	fmt.Println(x, y, z)

}
