package main

import "fmt"

const usixteenbitmax float64 = 65535
const kmh_multiple = 1.609

type car struct {
	gas_pedal uint16
	brake_pedal uint16
	steering_wheel int16
	top_speed_kmh float64
}

func (c car) kmh() float64 {
	return float64(c.gas_pedal) * (c.top_speed_kmh/usixteenbitmax)
}

func (c car) mph() float64 {
	return float64(c.gas_pedal) * (c.top_speed_kmh/usixteenbitmax/kmh_multiple)
}

func (c *car) new_top_speed(newspeed float64){
	c.top_speed_kmh = newspeed
}

func newer_top_speed(c car, newspeed float64) car{
	c.top_speed_kmh = newspeed
	return c
}

func newer_top_speed_ptr(c *car, newspeed float64){
	c.top_speed_kmh = newspeed
}

func main() {
	a_car := car{gas_pedal: 20000,
		brake_pedal:0,
		steering_wheel:-4,
		top_speed_kmh:225.0}

	fmt.Println(a_car.kmh())
	fmt.Println(a_car.mph())

	a_car.new_top_speed(250)
	fmt.Println(a_car.kmh())
	fmt.Println(a_car.mph())

	a_car = newer_top_speed(a_car, 225)
	fmt.Println(a_car.kmh())
	fmt.Println(a_car.mph())

	newer_top_speed_ptr(&a_car, 250)
	fmt.Println(a_car.kmh())
	fmt.Println(a_car.mph())
}
