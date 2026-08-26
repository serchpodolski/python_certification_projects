class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []
    self.balance = 0

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})
    self.balance += amount

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      self.balance -= amount
      return True
    return False

  def get_balance(self):
    return self.balance

  def transfer(self, amount, category):
    if self.withdraw(amount, f"Transfer to {category.name}"):
      category.deposit(amount, f"Transfer from {self.name}")
      return True
    return False

  def check_funds(self, amount):
    if amount > self.balance:
      return False
    return True

  def __str__(self):
    output = f"{self.name:*^30}\n"
    for item in self.ledger:
      output += f"{item['description'][:23]:23}{item['amount']:>7.2f}\n"
    output += f"Total: {self.balance:.2f}"
    return output

def create_spend_chart(categories):
  output = "Percentage spent by category\n"

  # 1. Calculate spent amount per category (withdrawals only)
  category_spends = []
  for category in categories:
      spent = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
      category_spends.append(spent)

  total_spent = sum(category_spends)

  # 2. Calculate percentages rounded down to the nearest 10
  percentages = []
  for spent in category_spends:
      if total_spent > 0:
          pct = int((spent / total_spent) * 100)
          percentages.append(pct - (pct % 10))
      else:
          percentages.append(0)

  # 3. Build the vertical chart (from 100 down to 0)
  for level in range(100, -1, -10):
      output += f"{level:>3}| "
      for pct in percentages:
          output += "o  " if pct >= level else "   "
      output += "\n"

  # 4. Build the horizontal line
  output += "    " + "-" * (len(categories) * 3 + 1) + "\n"

  # 5. Build vertical category names
  names = [category.name for category in categories]
  max_len = max(len(name) for name in names)

  for i in range(max_len):
      output += "     "
      for name in names:
          char = name[i] if i < len(name) else " "
          output += f"{char}  "
      if i < max_len - 1:
          output += "\n"

  return output

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(27.55, 'drugs')
print(food)
print(create_spend_chart([food, clothing]))