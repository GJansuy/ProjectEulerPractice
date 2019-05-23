from math import sqrt
from math import floor

# Borrowed from p7.py
def checkPrime(val: int):
  #v = val // 2
  v = floor(sqrt(val)) + 1 # Account for range's exclusion
  for i in range(2, v):
    if val % i == 0:
      return False
  return True

sum = 2 # Starting from 2
for i in range(3, 2000000, 2): # Avoid all evens
  if checkPrime(i):
    sum += i

print(sum)