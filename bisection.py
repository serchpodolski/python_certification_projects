def square_root_bisection(x, epsilon=0.0001, max_iterations=1000):
  """Returns the square root of x."""
  if x<0:
    raise ValueError("Square root of negative number is not defined in real numbers")
  if x==0 or x==1:
    print(f'The square root of {x} is {x}')
    return x

  low = 0.0
  high = max(1.0, float(x))
  for i in range(max_iterations):
    diff = high - low
    mid = (low + high) / 2.0
    if diff < epsilon:
      print(f'The square root of {x} is approximately {mid}')
      return mid
    elif mid**2 < x:
      low = mid
    else:
      high = mid

  print(f'Failed to converge within {max_iterations} iterations')
  return None

print(square_root_bisection(9))
print(square_root_bisection(987643621))
print(square_root_bisection(0.001, 1e-7, 50))
print( square_root_bisection(0.25, 1e-7, 50))