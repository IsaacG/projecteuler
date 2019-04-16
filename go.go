package main

import (
	"fmt"
)

// Q1: sum multiples of 3 and 5 under 1000
func Q1() int {
	m := 1000
	total := 0
	for i := 0; i < m; i++ {
		if (i % 3) == 0 || (i % 5) == 0 {
			total += i
		}
	}
	return total
}

// Q2: Sum of even Fibonnaci values under 4M
func Q2() int {
	m := 4000000
	a, b := 1, 2
	total := int(b)
	for (a+b) < m {
		c := (a+b)
		if (c % 2 == 0) {
			total += c
		}
		a, b = b, c
	}
	return total
}

// Q3: The prime factors of 13195 are 5, 7, 13 and 29.
// What is the largest prime factor of the number 600851475143 ?

func Q3() int {
	LargestPrime := func (n int) int {
		div := 2
		for div < n {
			for (n % div) == 0 {
				n /= div
			}
			div += 1
		}
		return n
	}
	return LargestPrime(600851475143)
}


// Q4: A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
// Find the largest palindrome made from the product of two 3-digit numbers.

func Q4() int {
	Reverse := func (s string) string {
		r := []rune(s)
		for i, j := 0, len(r)-1; i < len(r)/2; i, j = i+1, j-1 {
			r[i], r[j] = r[j], r[i]
		}
		return string(r)
	}

	IsPalindrome := func(x int) bool {
		s := fmt.Sprintf("%d", x)
		return s == Reverse(s)
	}

	Partial := func (high, low int) int {
		for i := high; i > low; i-- {
			if IsPalindrome(high*i) {
				return high*i
			}
		}
		return 0
	}

	MaxP := func(high, low int) int {
		max := 0
		for i := high; i > low; i-- {
			n := Partial(i, low)
			if n > max {
				max = n
			}
		}
		return max
	}

	return MaxP(999,900)
}

// 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

func Q5() int {
  IsDivByAll := func(n, d int) bool {
    for i := d; i > 1; i-- {
      if (n % i) != 0 {
        return false
			}
		}
    return true
	}

	var t int
  for t = 2520; ! IsDivByAll(t, 20); t += 2520 {
	}
  return t
}

func main() {
	ans := []func () int{Q1, Q2, Q3, Q4, Q5}
	for i, a := range ans {
		fmt.Printf("Q%d: %d\n", i+1, a())
	}
}

// vim:ts=2:sw=2:noexpandtab
