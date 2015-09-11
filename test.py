a = {'aa': 1, 'bb': 'ni'}
b = [3, 2, 1]
print a, b
print 'a' 'b''c'

for n, i in enumerate(["aa", "ii", "uu"]):
  if i == "aa":
    print n, i , "1234567890"[:-3]
  elif i == "ii":
    print n,i, "1234567890"[:-3][2:]
  else:
    print n,      i, "1234567890"[-3][2:][:1:2][:]
    print "ee""oo","ee\"\"oo"

print {x: x**2 for x in (2, 4, 6)}
print [x**2 for x in (2, 4, 6)]
print [x**3 for x in range(10) if x == x**2]

