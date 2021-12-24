// https://www.youtube.com/watch?v=hu0qcmbhH8s&list=PLCKpcjBB_VlBsxJ9IseNxFllf-UFEXOdg&index=43&ab_channel=AprendaGo

package main

import "fmt"

func main() {
	for i := 33; i <= 122; i++ {
		// fmt.Printf("%d\t%#x\t%#U\n", i, i, i)
		// fmt.Printf("%d - %v\n", i, string(i))
		fmt.Println(string(i))
		// transforming integers into string will not bring the number in quotation marks...
		// the warning message: conversion from int to string yields a string of one rune, not a string of digits (did you mean fmt.Sprint(x)?)
	}
	// I think that the ascii representation is the same as the integer/decimal representation
	// the unicode uses the same represetnation as the hexadecimal, and the hexadecimal translates
	// to a symbol
	// for the unicode there 4 place holders, each an contain 16 possible values, hexadecimal
	//
}
