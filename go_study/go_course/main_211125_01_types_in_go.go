// https://www.youtube.com/watch?v=C55_dhNmvrQ&list=PLCKpcjBB_VlBsxJ9IseNxFllf-UFEXOdg&index=23&ab_channel=AprendaGo

package main

import (
	"fmt"
)


func main(){

	a := "e"
	b := "é"
	fmt.Printf("%v, %T\n", a, a)
	fmt.Printf("%v, %T\n", b, b)

	d := []byte(a)
	e := []byte(b)

	fmt.Printf("%v, %T\n", d, d)
	fmt.Printf("%v, %T\n", e, e)

 // [] is called a slice of bytes


 	x := 10
	y := 10.0

	fmt.Printf("%v, %T\n", x, x)
	fmt.Printf("%v, %T\n", y, y)




}

// numeric types, int, float, 
// uint8
// uint16
// uint32
// uint64
// int8
// int16
// int32
// int64
// float32 = float
// float64 = double
// complex64
// complex128
// byte = uint8
// rune = int32

// there three possible modes in vim
// there: command mode, insert mode, visual mode




























