package main

import ("fmt"
	"sync"
)

var wg sync.WaitGroup

func foo(c chan int, somevalue int)  {
	defer wg.Done()
	c <- somevalue * 5
}

func main() {
	// buffer size is 10
	fooVal := make(chan int, 10)
	for i := 0; i < 10; i++{
		wg.Add(1)
		go foo(fooVal, i)
	}
	wg.Wait()
	close(fooVal)

	for item := range fooVal {
		fmt.Println(item)
	}
}
