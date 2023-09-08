def my_enumerate(iterable, start = 0):
  for i in iterable:
    yield start, i
    start += 1


