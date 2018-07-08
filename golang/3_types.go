package main

import "fmt"

func add(x, y float64) float64 {
	return x+y
}

func multiple(x, y string) (string, string) {
	return x, y
}
func main() {
	var num1 float64 = 5.6
	var num2 float64 = 9.5
	fmt.Println("add(5.6, 9.5)=", add(num1, num2))

	 //Type will be interpreted at compile time and it will never change
	 //the following function call will not work,
	 //if add accepts argument type of float32
	num3, num4 := 5.6, 9.5
	fmt.Println("add(5.6, 9.5)=", add(num3, num4))

	w1, w2 := "hey", "there!"
	fmt.Println(multiple(w1, w2))
}
