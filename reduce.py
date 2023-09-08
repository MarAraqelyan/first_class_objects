def my_reduce(function, iterable, initializer = None):
  result = iterable[0]
  for i in range(1, len(iterable)):
    result = function(result, i)
  if initializer is not None:
    result = function(result, initializer)
  return result 
     

