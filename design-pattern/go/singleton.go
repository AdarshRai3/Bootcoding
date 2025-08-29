// package main

// import "fmt"

// type Config struct{
// 	DBURL string
// }

// var instance *Config

// func GetConfig() *Config{
// 	if instance == nil {
// 		instance = &Config{DBURL:"postgress://"}
// 	}

// 	return instance
// }

// func main(){
// 	c1:= GetConfig()
// 	c2:=GetConfig()

// 	fmt.Println(c1==c2)//true
// }
// ----------------------------------------------------------------------
package main

import (
	"fmt"
	"sync"
)

type Config struct{
  DBURL string
}

var(
	once sync.Once
	instance *Config
)

func GetConfig() *Config{
	once.Do(func(){
		fmt.Println("Creating new Config")
		instance = &Config{DBURL:"postgres://"}

	})

	return instance 
}

func main(){
	c1:= GetConfig()
	c2:= GetConfig()
	fmt.Println(c1==c2)//true
}

//sync.Once guarantees that the function inside only run once 
