module Main (main) where
import Prelude
import Text.Printf

-- Q1: sum multiples of 3 and 5

good :: Int -> Bool
good x = (mod x 3 == 0) || (mod x 5 == 0)

try = [1,2..999]
valid = filter good try
ans1 = sum valid

-- Q2: sum Fibonacci

-- Build a list of Fibonacci values as long as they are under `max`
fib :: Int -> [Int] -> [Int]
fib max (a:b:xs) = if a+b >= max then (a:b:xs) else fib max ((a+b):a:b:xs)

ans2 = sum $ filter (\x -> mod x 2 == 0 ) $ fib 4000000 (2:1:[])


-- Q3: The prime factors of 13195 are 5, 7, 13 and 29.
-- What is the largest prime factor of the number 600851475143 ?

-- Q3 take1 (not used)
isDiv :: Int -> Int -> Bool
isDiv x y = mod x y == 0

factors :: Int -> [Int]
factors x = filter (isDiv x) [1,2..x]

prime :: Int -> Bool
prime x = (factors x) == [1,x]

primeFactors :: Int -> [Int]
primeFactors x = filter prime $ factors x
-- Waaaaaaay too slow

-- Q3 take2
reduce :: Int -> [Int] -> Int
reduce n (a:xs)
  | a < n = if mod n a == 0 then reduce (div n a) xs else reduce n xs
  | otherwise = n
ans3 = reduce 600851475143 (2:[3,5..])

-- Q4: A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
-- Find the largest palindrome made from the product of two 3-digit numbers.

isPalin :: Int -> Bool
isPalin x = let y = show x in y == reverse y

listMax :: [Int] -> Int
listMax (x:xs) = max x $ listMax xs
listMax [] = 0

-- Return the first palindrome found by multiplying fixed*[changes, changes-1 ... changes - N ... min]
makePalin :: Int -> Int -> Int -> Int
makePalin fixed changes min
  | isPalin (fixed * changes) = fixed * changes
  | changes <= min = 0
  | otherwise = makePalin fixed ( changes - 1 ) min

ans4 = listMax $ map (\x -> makePalin x x 900) [999,998..900]

allPalin :: Int -> Int -> [Int]
allPalin max min
  | max >= min = (makePalin max max min):(allPalin (max - 1) min)
  | otherwise = []

ans4b = listMax $ allPalin 999 900

-- Answer printing

showAns :: Int -> Int -> IO ()
showAns x y = printf "Q%d: %d\n" x y

main = do
  showAns 1 ans1
  showAns 2 ans2
  showAns 3 ans3
  showAns 4 ans4
