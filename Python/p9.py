# a < b < c and a^2 + b^2 = c^2
for c in range(2, 1000): # There are better starting points...
  for b in range(1, c):  # But I'm not sure where to justifiably start
    if c - b > b: continue # Avoid immediately invalid cases
    for a in range(c-b, b):
      if a + b + c == 1000: # Most exclusive aspect
        if a*a + b*b == c*c: # pythogrean triplet
          print(a,b,c, a * b * c)
          exit()
