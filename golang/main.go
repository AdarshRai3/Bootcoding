package main

import (
	"fmt"
)

func add (x int , y int ) int {
	return x + y
}

func swap(x, y string) (string , string){
   return y , x;
}

func split(sum int)(int , int){
	x := sum * 4/9
	y := sum - x 
	return x ,y 
}

var c , python , java bool

func main() {
	var j int
	i:=7
	fmt.Println(i , j ,c , python , java)
	fmt.Println("Hello, World!")
	fmt.Println("Sum of two numbers ",add(32,18))
    x, y := swap("Simple", "Stupid")
	fmt.Println("Swap two strings:",y,x)
	fmt.Println(split(18))
}