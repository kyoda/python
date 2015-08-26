
for i in ["aa", "ii", "uu"]:
  if i == "aa":
    print i , "1234567890"[:1:]
  elif i == "ii":
    print i,"1234567890"[:-3]
  else:
    print i,    "1234567890"[-3:]
