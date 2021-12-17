// https://www.youtube.com/watch?v=onK_nd--g1g&list=PLCKpcjBB_VlBsxJ9IseNxFllf-UFEXOdg&index=31&ab_channel=AprendaGo
// escreva um programa que mostre um número em decimal, binário e hexadecimal
package main

import "fmt"

func main() {
	myNumber := 77
	// expected:
	// binary: 0b1001101
	// hexadecimal: 0x4d

	fmt.Printf("%v | %#b | %#x\n", myNumber, myNumber, myNumber)
}
