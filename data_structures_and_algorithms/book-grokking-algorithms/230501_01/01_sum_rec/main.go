package main

import "fmt"

func main() {

	myArr := []int{1, 2, 3}
	fmt.Println("sumArrLoop(myArr) = ", sumArrLoop(myArr))

	fmt.Println("sumArrRec(myArr, 0) = ", sumArrRec(myArr, 0))
}

func sumArrLoop(arr []int) int {
	total := 0
	for _, val := range arr {
		total += val
	}
	return total
}

func sumArrRec(arr []int, prevSum int) int {
	if len(arr) == 0 {
		return 0
	} else if len(arr) == 1 {
		return arr[0] + prevSum
	}
	lastVal := arr[len(arr)-1]
	currSum := prevSum + lastVal
	newArr := arr[:len(arr)-1]

	return sumArrRec(newArr, currSum)
}
