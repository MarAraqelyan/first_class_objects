def my_zip(*iterables, strict = False):
  if len(iterables) == 0:
     return iterables

  if strict:
    for i in range(len(iterables) - 1):
      if iterables[i] != iterables[i + 1]:
        raise ValueError("zip() arguments must be the same size")

  Min = len(iterables[0])
  for i in range(1, len(iterables)):
    if len(iterables[i]) < Min:
      Min = len(iterables[i])
  for i in range(Min):
    yield [x[i] for x in iterables]



