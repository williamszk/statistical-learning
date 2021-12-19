// https://www.youtube.com/watch?v=8zEZw19gRTo&list=PLCKpcjBB_VlBsxJ9IseNxFllf-UFEXOdg&index=32&ab_channel=AprendaGo
// escreva experessões usando os seguitnes operadores, e atribua seus valores a variáveis
// ==
// !=
// <=
// <
// >
// >=
package main

import "fmt"

func main() {

	myNumber1 := 10.98
	myNumber2 := 87.22

	myEqual := myNumber1 == myNumber2
	fmt.Println("myEqual = ", myEqual)

	myDifferent := myNumber1 != myNumber2
	fmt.Println("myDifferent = ", myDifferent)

	myLessOrEqual := myNumber1 <= myNumber2
	fmt.Println("myLessOrEqual = ", myLessOrEqual)

	myLessThan := myNumber1 < myNumber2
	fmt.Println("myLessThan = ", myLessThan)

	myGreaterOrEqual := myNumber1 >= myNumber2
	fmt.Println("myGreaterOrEqual = ", myGreaterOrEqual)

	myGreaterThan := myNumber1 > myNumber2
	fmt.Println("myGreaterThan = ", myGreaterThan)

}
