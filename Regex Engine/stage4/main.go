package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func checkChar(regex, char string) bool {
	if regex == "" || char == regex || (regex == "." && char != "") {
		return true
	}
	return false
}

func endOfComparison(regex, word string) bool {
	if !checkChar(string(regex[0]), string(word[0])) {
		return false
	}

	if checkStr(regex[1:], word[1:]) {
		return true
	}
	return false
}

func fullScanComparison(regex, word string) bool {
	for w := range word {
		if checkStr(regex, word[w:]) {
			return true
		}
	}
	return false
}

func compare(regex, word string) bool {
	if regex == "" {
		return true
	}

	// Add a "new check" for the first special case; if the regex begins with the '^' character:
	if regex[0] == '^' {
		if checkStr(regex[1:], word) {
			return true
		}
	}
	return fullScanComparison(regex, word)
}

func checkStr(regex, word string) bool {
	// Add another "new check" for the second special case; if the regex ends with the the '$' character:
	if regex == "" || (regex == "$" && word == "") {
		return true
	}

	if word == "" {
		return false
	}

	if endOfComparison(regex, word) {
		return true
	}

	return false
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

	fmt.Println(compare(regex, word))
}
