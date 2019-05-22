
NUMBER = 600851475143 # Prompted number

primes = []

# Remove any possible twos first off

while NUMBER % 2 == 0:
  primes.append(2)
  NUMBER = NUMBER / 2

# Number is now odd
# Starts from next prime, 3, ignore evens
for i in range(3, NUMBER, 2):
  while NUMBER % i == 0: # There must be more efficient ways of doing this...
    primes.append(i)
    NUMBER = NUMBER / i
  if NUMBER == 1: # The number has been fully consumed
    break

print(primes)