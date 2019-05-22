DESIRED_INDEX = 10001

index = 2
i = 3

def checkPrime(val: int):
  v = val // 2
  for i in range(2, v):
    if val % i == 0:
      return False
  return True


while index != DESIRED_INDEX:
  i += 2
  if checkPrime(i):
    index += 1 

print(i)