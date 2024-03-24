package module1_test

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"isuct.ru/informatics2022/internal/module3"
)

func TestHash(t *testing.T) {
	assert := assert.New(t)
	t.Run("Hash", func(t *testing.T) {
		t.Run("Test hash AB", func(t *testing.T) {
			hash := module3.Hash("AB", 7, 3)
			assert.Equal(1, hash)
		})
		t.Run("Test hash CB", func(t *testing.T) {
			hash := module3.Hash("CB", 7, 3)
			assert.Equal(0, hash)
		})
		t.Run("Test hash ABBA", func(t *testing.T) {
			hash := module3.Hash("ABBA", 7, 3)
			assert.Equal(5, hash)
		})
		t.Run("Test hash ABBC", func(t *testing.T) {
			hash := module3.Hash("ABBC", 7, 3)
			assert.Equal(0, hash)
		})
	})
	t.Run("Sliding Hash", func(t *testing.T) {
		hash := module3.Hash("ABBA", 7, 3)
		thash := module3.Hash("BBAC", 7, 3)
		sHash, nStr := module3.SlidingHash(hash, 'C', "ABBA", 7, 3)
		assert.Equal(nStr, "BBAC")
		assert.Equal(thash, sHash)
	})
	t.Run("Sliding Hash", func(t *testing.T) {
		hash := module3.Hash("BBBB", 7, 3)
		sHash, nStr := module3.SlidingHash(hash, 'B', "BBBB", 7, 3)
		assert.Equal(nStr, "BBBB")
		assert.Equal(hash, sHash)
	})
}
