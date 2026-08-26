class GameCharacter:
  def __init__(self, name):
    self._name = name
    self.health = 100
    self.mana = 50
    self._level = 1

  def __str__(self):
    return f"Name: {self._name}\nLevel: {self._level}\nHealth: {self._health}\nMana: {self._mana}"

  @property
  def name(self):
    return self._name

  @property
  def health(self):
    return self._health

  @property
  def mana(self):
    return self._mana

  @property
  def level(self):
    return self._level

  @health.setter
  def health(self, new_health):
    if 0 <= new_health <= 100:
      self._health = new_health
    if new_health < 0:
      self._health = 0

  @mana.setter
  def mana(self, new_mana):
    if 0 <= new_mana <= 50:
      self._mana = new_mana
    if new_mana < 0:
      self._mana = 0

  def level_up(self):
    self._level += 1
    self.health = 100
    self.mana = 50
    print(f"{self._name} leveled up to {self._level}!")

hero = GameCharacter('Kratos') # Creates a new character named Kratos
print(hero)  # Displays the character's stats

hero.health -= 30  # Decreases health by 30
hero.mana -= 10    # Decreases mana by 10
print(hero)  # Displays the updated stats

hero.level_up()  # Levels up the character
print(hero)