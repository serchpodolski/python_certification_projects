class Rectangle:
  def __init__(self, width, height):
    self._width = width
    self._height = height

  def __str__(self):
    return f'Rectangle(width={self._width}, height={self._height})'

  def set_width(self, new_width):
    self._width = new_width

  def set_height(self, new_height):
    self._height = new_height

  def get_area(self):
    return self._width * self._height

  def get_perimeter(self):
    return 2 * (self._width + self._height)

  def get_diagonal(self):
    return ((self._width ** 2 + self._height ** 2) ** 0.5)

  def get_picture(self):
    if self._width > 50 or self._height > 50:
      return 'Too big for picture.'
    return (('*' * self._width + '\n') * self._height)

  def get_amount_inside(self, shape):
    return (self._width // shape._width) * (self._height // shape._height)

class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side, side)

  def __str__(self):
    return f'Square(side={self._width})'

  def set_side(self, new_side):
    self._width = new_side
    self._height = new_side

  def set_width(self, new_side):
    self._width = new_side
    self._height = new_side

  def set_height(self, new_side):
    self._width = new_side
    self._height = new_side

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))