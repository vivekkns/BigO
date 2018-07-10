package main

import "fmt"

func foo(c chan int, somevalue int)  {
	c <- somevalue * 5
}

func main() {
	fooVal := make(chan int)
	go foo(fooVal, 5)
	go foo(fooVal, 10)

	//v1 := <-fooVal
	//v2 := <-fooVal

	v1, v2 := <-fooVal, <-fooVal

	fmt.Println(v1, v2)
}
