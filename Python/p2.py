LIMIT = 4000000 # Do not exceed four million

counter = 0

# Base Cases
first = 1 
last = 1

while last < LIMIT:
  last, first = (first + last, last) # Sequence Unpacking
  if last % 2 == 0:
    counter += last

print(counter)