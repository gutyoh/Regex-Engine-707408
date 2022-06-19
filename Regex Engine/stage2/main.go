package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func checkChar(regex, char string) bool {
	if regex == "" {
		return true
	} else if char == regex {
		return true
	} else if regex == "." && char != "" {
		return true
	} else {
		return false
	}
}

// New function checkStr, will help us check for checking strings apart from chars
func checkStr(regex, word string) bool {
	if regex == "" {
		return true
	} else if word == "" || !checkChar(regex[0:1], word[0:1]) {
		return false
	} else if checkStr(regex[1:], word[1:]) {
		return true
	} else {
		return false
	}
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()

	// if scanner.Text() doesn't contain the "|" symbol, exit the program:
	if !strings.Contains(scanner.Text(), "|") {
		fmt.Println(false)
		return
	}

	// if scanner.Text() contains the | symbol, split 'line' by the | symbol and continue with the program:
	line := strings.Split(scanner.Text(), "|")
	regex, word := line[0], line[1]

	fmt.Println(checkStr(regex, word))
}
