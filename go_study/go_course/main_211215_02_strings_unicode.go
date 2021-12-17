// https://www.youtube.com/watch?v=AcyS0_BAy7U&list=PLCKpcjBB_VlBsxJ9IseNxFllf-UFEXOdg&index=26&ab_channel=AprendaGo
// Strings
package main

import "fmt"

func main() {
	myString := "Hello Playground!"
	fmt.Println(myString)
	// formated strings
	fmt.Printf("%v | %T\n", myString, myString)

	// using strange string formating
	myStringStrangeFormating := `Hello,
					playground
			this is a strange

			string!.`

	fmt.Printf("%v\n", myStringStrangeFormating)

	// what are byte slice?
	sliceBytesMyString := []byte(myString)
	fmt.Printf("%v, %T\n", sliceBytesMyString, sliceBytesMyString)

	// just another test with byte slice
	myAnotherString := "ABC"
	byteSliceMyAnotherString := []byte(myAnotherString)
	fmt.Printf("%v, %T\n", byteSliceMyAnotherString, byteSliceMyAnotherString)
	// [65 66 67], []uint8
	//

	for _, v := range byteSliceMyAnotherString {
		fmt.Printf("%v, %T\n", v, v)
	}
	fmt.Println("========================================================================")
	// show unicode of each character
	// show hexadecimal representation
	for _, v := range byteSliceMyAnotherString {
		fmt.Printf("%v | %T | %#U | %#x\n", v, v, v, v)
	}
	fmt.Println("========================================================================")
	for i := 0; i < len(byteSliceMyAnotherString); i++ {
		fmt.Printf("%v | %T | %#U | %#x\n", byteSliceMyAnotherString[i], byteSliceMyAnotherString[i], byteSliceMyAnotherString[i], byteSliceMyAnotherString[i])
	}
	fmt.Println("========================================================================")
	fmt.Println("Let's use some unicode character inside the string to see how the %#U and %#x behave...")
	myStringUnicodeExample := "♥💀🤖"
	byteSliceMyStringUnicodeExample := []byte(myStringUnicodeExample)
	for _, v := range byteSliceMyStringUnicodeExample {
		fmt.Printf("%v | %T | %#U | %#x\n", v, v, v, v)
	}
	fmt.Println("")
	for i := 0; i < len(byteSliceMyStringUnicodeExample); i++ {
		fmt.Printf("%v | %T | %#U | %#x\n", byteSliceMyStringUnicodeExample[i], byteSliceMyStringUnicodeExample[i], byteSliceMyStringUnicodeExample[i], byteSliceMyStringUnicodeExample[i])
	}
	fmt.Println("In the case of using unicode characters the byte representation is much stranger...")
	fmt.Println("========================================================================")
}
