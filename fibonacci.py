def fibonacci(n):
  sequence = [0, 1]

  if n <= 1:
    return sequence[n]

  for i in range(2, n+1):
    sequence.append(sequence[i - 1] + sequence[i - 2])

  print(sequence)
  return sequence[n]

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(5))
print(fibonacci(10))
print(fibonacci(15))
