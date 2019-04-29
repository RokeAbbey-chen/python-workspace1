def choose(l, pick):
  if pick == 0:
    yield []
    return
  for i in xrange(len(l)):
    item = l[i]
    for l2 in choose(l[(i+1):], pick-1):
      l2.insert(0, item)
      yield l2
      del l2[0]


print(choose(range(4), 2))