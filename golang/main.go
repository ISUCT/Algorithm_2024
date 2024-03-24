package main

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"math"
	"os"
	"strconv"
	"strings"
)

func Hash(inp string, p, x float64) int {
	hash := 0
	for _, symbol := range inp {
		hash = (hash*int(x) + int(symbol-rune('A'))) % int(p)
	}
	return hash
}

func SlidingHash(hash int, newSymbol rune, oldString string, p, x float64) (int, string) {
	nHash := int(float64(hash)*x-float64((oldString[0]-byte('A')))*math.Pow(x, float64(len(oldString)))+float64(newSymbol-'A')) % int(p)
	nHash = (nHash + int(p)) % int(p)
	return nHash, (oldString[1:] + string(newSymbol))
}

func RabinCarp() {
	p := float64(1000007)
	x := float64(37)
	reader := bufio.NewReader(os.Stdin)
	s, err := reader.ReadString('\n')
	s = strings.TrimSuffix(s, "\n")
	s = strings.TrimSuffix(s, "\r")
	if err != nil {
		log.Fatal(err)
	}
	t, err := reader.ReadString('\n')
	t = strings.TrimSuffix(t, "\n")
	t = strings.TrimSuffix(t, "\r")
	if err != nil && err != io.EOF {
		log.Fatal(err)
	}
	hash_s := Hash(s[0:len(t)], p, x)
	hash_t := Hash(t, p, x)
	idx := []string{}
	substr := s[0:len(t)]
	for i := 0; i <= len(s)-len(t); i++ {
		if hash_s == hash_t {
			if t == s[i:i+len(t)] {
				idx = append(idx, strconv.Itoa(i))
			}
		}
		if i+len(t) < len(s) {
			hash_s, substr = SlidingHash(hash_s, rune(s[i+len(t)]), substr, p, x)
		}
	}
	res := strings.Join(idx, " ")
	fmt.Println(res)
}

func main() {
	RabinCarp()
}
