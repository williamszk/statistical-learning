// https://www.youtube.com/watch?v=Ma3M7Pdd7HI&list=PLCKpcjBB_VlBsxJ9IseNxFllf-UFEXOdg&index=27&ab_channel=AprendaGo

package main

import "fmt"

// go conversion of decimal to binary and hexadecimal

func main() {

	myDecimal := 100

	fmt.Printf("%d\t%b\t%x\n", myDecimal, myDecimal, myDecimal)

	// we can also include a # sign so that we have 0b or 0x before the number

	fmt.Printf("%v\t%d\t%#b\t%#x\n", myDecimal, myDecimal, myDecimal, myDecimal)
}

// next class
// https://www.youtube.com/watch?v=Yaw80pKukMc&list=PLCKpcjBB_VlBsxJ9IseNxFllf-UFEXOdg&index=28&ab_channel=AprendaGo
