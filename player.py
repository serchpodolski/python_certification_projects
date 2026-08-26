from abc import ABC, abstractmethod
import random

class Player(ABC):
  def __init__(self):
    self.moves = []
    self.position = (0, 0)
    self.path = [self.position]

  def make_move(self):
    if not self.moves:
      raise ValueError("No valid moves available")
    dx, dy = random.choice(self.moves)
    current_x, current_y = self.position
    self.position = (current_x + dx, current_y + dy)
    self.path.append(self.position)
    return self.position

  @abstractmethod
  def level_up(self):
    pass

class Pawn(Player):
  def __init__(self):
    super().__init__()
    self.moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]

  
  def level_up(self):
    diagonal_moves = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for move in diagonal_moves:
      if move not in self.moves:
        self.moves.append(move)
    print("Pawn leveled up! Diagonal movement unlocked.")

if __name__ == '__main__':
  pawn = Pawn()
  print(f"Start Position: {pawn.position}")
  
  # Make 3 random moves
  for _ in range(3):
    pawn.make_move()
  
  print(f"Path after basic moves: {pawn.path}")
  
  # Level up to unlock diagonal movements
  pawn.level_up()
  print(f"Available moves after level up ({len(pawn.moves)} total): {pawn.moves}")
  
  # Make 3 diagonal moves
  for _ in range(3):
    pawn.make_move()
  
  print(f"Path after diagonal moves: {pawn.path}")
