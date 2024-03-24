package module1_test

import (
	"io"
	"log"
	"os"
	"testing"

	"github.com/stretchr/testify/assert"
	"isuct.ru/informatics2022/internal/module3"
	"isuct.ru/informatics2022/tests/helpers"
)

func TestRabinCarp(t *testing.T) {
	assert := assert.New(t)

	defer func(v *os.File) {
		os.Stdin = v
	}(os.Stdin)
	defer func(v *os.File) { os.Stdout = v }(os.Stdout)
	t.Run("Test rabin carp", func(t *testing.T) {
		r, w := helpers.Replacer(`ababbababa
aba
`, t)
		os.Stdin = r
		os.Stdout = w

		module3.RabinCarp()
		w.Close()
		out, _ := io.ReadAll(r)
		assert.Equal(`0 5 7
`, string(out))
	})
	t.Run("Test rabin carp 2", func(t *testing.T) {
		file, err := os.OpenFile("02", os.O_RDONLY, 0644)
		if err != nil {
			log.Fatal(err)
		}
		r, w, err := os.Pipe()
		if err != nil {
			t.Fatal(err)
		}

		os.Stdin = file
		os.Stdout = w

		module3.RabinCarp()
		w.Close()
		out, _ := io.ReadAll(r)
		r.Close()
		assert.Equal(`287 1585 3612 4294 10800 12025 20604 26894
`, string(out))
	})
	t.Run("Test rabin carp 10", func(t *testing.T) {
		file, err := os.OpenFile("10", os.O_RDONLY, 0644)
		if err != nil {
			log.Fatal(err)
		}
		r, w, err := os.Pipe()
		if err != nil {
			t.Fatal(err)
		}

		os.Stdin = file
		os.Stdout = w

		module3.RabinCarp()
		w.Close()
		out, _ := io.ReadAll(r)
		assert.Equal(`0 1 2
		`, string(out))
	})
}
