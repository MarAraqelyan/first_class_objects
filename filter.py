def my_filter(function, iterable):
  if function is None:
    for i in iterable:
      if i:
        yield i
  else:
    for i in iterable:
      if function(i):
        yield i


