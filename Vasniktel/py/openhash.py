import hashbase

class OpenHash(hashbase.HashBase):
  def __init__(self, size, hashFunc):
    super(OpenHash, self).__init__(size, hashFunc)

  def __setitem__(self, key, value):
    for i in xrange(self.size):
      index = self._hash(key, self.size, i)

      if self._table[index] is None:
        self._table[index] = [key, value]
        break
      else:
        self.collisions += 1

    else: raise Exception('Table is full')

  def __getitem__(self, key):
    for i in xrange(self.size):
      index = self._hash(key, self.size, i)

      entry = self._table[index]
      if entry is None: break
      elif entry[0] == key: return entry[1]

    return None
