#import math

LIMIT = 1000 # 3 Digit numbers

def checkPalindrome(val: int):

  # Had an idea with using logarithms and integer division, a bit messy
  #fastone = (val // (10 ** math.floor( math.log10(val) ) ) )
  #fasttwo = val % 10
  #if fastone != fasttwo:
  #  return False

  temp = val
  rev = 0
  while temp > 0:
    
    rev = int(rev * 10) # Make space
    rev =  rev + int(temp % 10) # Get a digit
    temp =  temp // 10 # Cut off that digit

  if val == rev:
    return True
  else:
    return False

# The product of two, 3-digit numbers
largest = 0

for i in range(LIMIT//10, LIMIT):
  for j in range(i, LIMIT): # Multiplication is commutative, avoid duplicates, start at i
    #print( i, j, i*j)
    v = i * j
    if checkPalindrome(v):
      if largest < v:
        largest = v

print(largest)