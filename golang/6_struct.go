package main

import "fmt"

type car struct {
	gas_pedal uint16
	brake_pedal uint16
	steering_wheel int16
	top_speed_kmh float64
}


func main() {
	var c_car car
	c_car.top_speed_kmh = 250

	fmt.Println(c_car.top_speed_kmh, c_car.brake_pedal)

	a_car := car{gas_pedal: 15,
		brake_pedal:1,
		steering_wheel:-4,
		top_speed_kmh:100}
	fmt.Println(a_car.gas_pedal)

	b_car := car{14, 1, -4, 200}
	fmt.Println(b_car.steering_wheel)
}
