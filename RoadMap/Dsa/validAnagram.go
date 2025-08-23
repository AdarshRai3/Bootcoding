package main

import (
	"unicode"
)

func isAnagram(s string,t string) bool{
	if len(s)!=len(t){
		return false
	}

	freq := make(map[rune]int)
	for _,ch := range s{
		if unicode.IsSpace(ch){
			continue
		}

		freq[ch]++
	}

	for _,ch := range t{
		if unicode.IsSpace(ch){
			continue
		}
		freq[ch]--
		if(freq[ch]<0){
			return false
		}
	}

	for _,count := range freq{
		if count != 0 {
			return false
		}
	}

	return true
}