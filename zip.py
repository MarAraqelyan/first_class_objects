def my_zip(*iterables, strict = False):
  if len(iterables) == 0:
<<<<<<< HEAD
    return  
=======
     return 
>>>>>>> 0c1552d2d4aeaae3768623c9834c694cf5415c85

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



