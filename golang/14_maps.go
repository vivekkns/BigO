package main

import "fmt"

func main() {
	grades := make(map[string]float32)

	grades["vivek"] = 45
	grades["guna"] = 56
	grades["kani"] = 78

	fmt.Println(grades)

	vivek_grade := grades["vivek"]
	fmt.Println("vovek's grade:", vivek_grade)

	delete(grades, "vivek")
	fmt.Println(grades)

	for k,v := range grades {
		fmt.Println(k, ":", v)
	}
}