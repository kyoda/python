a = {'aa': 1, 'bb': 'ni'}
print a['aa']
print a

for i in ["aa", "ii", "uu"]:
  if i == "aa":
    print i , "1234567890"[:-3]
  elif i == "ii":
    print i, "1234567890"[:-3][2:]
  else:
    print i, "1234567890"[-3][2:][:1:2][:]
    print "ee""oo","ee\"\"oo"
