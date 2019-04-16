#  Q1: sum multiples of 3 and 5 under 1000
def Q1():
  m = 1000
  total = 0
  for i in range(m):
    if (i % 3) == 0 or (i % 5) == 0:
      total += i
  print('Q1: %d' % total)

# Q2: Sum of even Fibonnaci values under 4M
def Q2():
  m = 4000000
  a, b = 1, 2
  total = a + b
  while (a+b) < m:
    c = (a+b)
    if c % 2 == 0:
      total += c
    a, b = b, c
  print('Q2: %d' % total)


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
  print('Q3: %d' % LargestPrime(600851475143))


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

  print('Q4: %d' % MaxP(999,900))

  


Q1()
Q2()
Q3()
Q4()
