def hanoi_solver(n):
  pegs = {
    "A": list(range(n, 0, -1)),
    "B": [],
    "C": []
  }
  result = ''

  def print_state():
    return f'{pegs["A"]} {pegs["B"]} {pegs["C"]}\n'

  def move_disks(count, source, target, aux):
    nonlocal result
    if count == 1:
      disk = pegs[source].pop()
      pegs[target].append(disk)
      result += print_state()
      return

    move_disks(count - 1, source, aux, target)

    disk = pegs[source].pop()
    pegs[target].append(disk)
    result += print_state()

    move_disks(count-1, aux, target, source)

  result += print_state()
  move_disks(n, "A", "C", "B")
  return result.rstrip('\n')

print(hanoi_solver(2) + '\n\n')
print(hanoi_solver(3) + '\n\n')
print(hanoi_solver(4) + '\n\n')
print(hanoi_solver(5) + '\n\n')