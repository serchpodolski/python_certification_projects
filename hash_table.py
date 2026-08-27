class HashTable:
  def __init__(self):
    self.collection = {}

  def hash(self, string_to_hash: str):
    return sum(map(ord, string_to_hash))

  def add(self, key, value):
    hashed_key = self.hash(key)
    # print(hashed_key_dict)
    if hashed_key not in self.collection:
      self.collection[hashed_key] = { key : value }
    else:
      self.collection[hashed_key].update({ key : value })

  def remove(self, key):
    hashed_key = self.hash(key)
    if hashed_key in self.collection and key in self.collection[hashed_key]:
      del self.collection[self.hash(key)][key]
      if not self.collection[hashed_key]:
        del self.collection[hashed_key]
    
  def lookup(self, key):
    hashed_key = self.hash(key)
    if hashed_key in self.collection:
      return self.collection[hashed_key].get(key, None)
    return None

my_hash = HashTable()
print(my_hash.hash('golf'))
print(my_hash.add('golf', 'sport'))
print(my_hash.add('logf', 'wayoflife'))
print(my_hash.lookup('golf'))
print(my_hash.lookup('logf'))
print(my_hash.collection)