LIMIT = 100

u = 0
q = 0
for i in range(1,LIMIT+1):
  u += i
  q += (i ** 2)

u *= u

print (u-q)