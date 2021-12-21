// https://www.youtube.com/watch?v=NxntmGW62Ag&list=PLCKpcjBB_VlBsxJ9IseNxFllf-UFEXOdg&index=34&ab_channel=AprendaGo
// atribua valor int a uma variavel
// print o valor em decimal, binary e hexadecimal
// desloque um bit dessa variável para esquerda e atribua o resultado para uma nova variável
// demostre essa nova variável em decimal, binario e hexadecimal

package main

import "fmt"

func main() {
	myNumber1 := 10
	fmt.Printf("%d, %#b, %#x\n", myNumber1, myNumber1, myNumber1)

	myNumber2 := myNumber1 << 1
	fmt.Printf("%d, %#b, %#x\n", myNumber2, myNumber2, myNumber2)

}
