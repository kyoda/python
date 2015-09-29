
def add(x, y):
  return x + y


print add(111, 222)

dic = {'name': 'machida', 'age': 17, 'num': [1, 2, 3, 4]}
for n, i in enumerate(dic):
  print "%d: %s => %s" % (n, i, dic[i])

for key, value in dic.iteritems():
  print "%s: %s" % (key, value)

arr = [1, 2, 'age',  3, 4, 5, 6, 'name']
for n, i in enumerate(arr):
  print '%s: %s' % (n, i)

#a = {'name': [1, 2, 3, 4, 5], 'bb': 'ni'}
#b = [3, 2, 1]
#for n, i in enumerate(a):
#  print 'machida'
#  print n, i, a[i]
#
#for i in a:
#  print i
#
#print a['name']
#print 'a' 'b''c'
#
#print {x: x**2 for x in (2, 4, 6, 8 ,10)}
#print [x**2 for x in (2, 4, 6)]
#print [x**3 for x in range(10) if x == x**2]
#
#for n, i in enumerate(["aa", "ii", "uu"]):
#
#  if i == "uu":
#    print n, i , "1234567890"[:-3]
#  elif i == "aa":
#    print n,i, "1234567890"[:-3][2:]
#  else:
#    print n,      i, "1234567890"[-3][2:][:1:2][:]
#    print "ee""oo","ee\"\"oo"
#
#
#
#    print "in else"
#  print "in for"
#print "out"

