#!/bin/python

import inspect
import sys

#  Q1: sum multiples of 3 and 5 under 1000
def Q1():
  m = 1000
  total = 0
  for i in range(m):
    if (i % 3) == 0 or (i % 5) == 0:
      total += i
  return total

# Q2: Sum of even Fibonnaci values under 4M
def Q2():
  m = 4000000
  a, b = 1, 2
  total = b
  while (a+b) < m:
    c = (a+b)
    if c % 2 == 0:
      total += c
    a, b = b, c
  return total


# Q3: The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def Q3():
  def LargestPrime(n):
    div = 2
    while div < n:
      while (n % div) == 0:
        n //= div
      div += 1
    return n
  return LargestPrime(600851475143)


# Q4: A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def Q4():

  def IsPalindrome(x):
    return str(x) == str(x)[::-1]

  def Partial(high, low):
    for i in range(high, low, -1):
      if IsPalindrome(high*i):
        return [high*i]
    return []

  def MaxP(high, low):
    got = []
    for i in range(high, low, -1):
      got += Partial(i, low)
    return sorted(got)[-1]

  return MaxP(999,900)

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def Q5():

  def IsDivByAll(n, d):
    i = d
    while i > 1:
      if n % i:
        return False
      i -= 1
    return True

  t = 2520
  while not IsDivByAll(t, 20):
    t += 2520
  return t

if __name__ == '__main__':
  me = sys.modules[__name__]
  for n,f in inspect.getmembers(me, inspect.isfunction):
    if not n.startswith('Q'):
      continue
    print('%s: %d' % (n, f()))


# vim:ts=2:sw=2:expandtab
