# Smallest Multiple

LIMIT = 20
STARTING_POINT = LIMIT # We have to start somewhere

def checkRange(val: int):
  if val % LIMIT != 0:
    return False # Disregard anything that isn't divisible by at least the limit
  for i in range(2, LIMIT+1): # 1 is implied divisible
    #print(val ,val % i, i)
    if val % i != 0:
      return False
  return True

while not checkRange(STARTING_POINT):
  STARTING_POINT += 2 # All odds automatically disqualify

print(STARTING_POINT)