package main

import (
	"fmt"
	"strings"
)

func sumSlice(nums []int) int{
	sum:= 0

	for _, num := range nums{
		sum += num
	}

	return sum
}

func countWord(text string)map[string]int{
	freq := make(map[string]int)
	words := strings.Fields(text)
    
	for _, word := range words {
		freq[word]++
	}
	return freq
}

func charCount(s string) map[rune]int{
	freq := make(map[rune]int)

	for _,ch := range s{
		freq[ch]++
	}

	return freq
}
func main() {
	arr := []int {1,2,3,4,5}
	fmt.Println(sumSlice(arr))

	text := "go is fun and go is powerful, I love go"
	result := countWord(text)
	ans := charCount(text)
	fmt.Println(ans)
	fmt.Println(result)

	for ch, count := range ans{
		fmt.Printf("%c: %d\n",ch,count)
	}
} 



