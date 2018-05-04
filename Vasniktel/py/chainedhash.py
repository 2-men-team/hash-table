import hashbase

class ChainedHash(hashbase.HashBase):
  def __init__(self, size, hashFunc):
    super(ChainedHash, self).__init__(size, hashFunc)

  def __setitem__(self, key, value):
    index = self._hash(key, self.size)

    data = [key, value]
    if self._table[index] is None:
      self._table[index] = [data]
    else:
      self._table[index].append(data)
      self.collisions += 1

  def __getitem__(self, key):
    index = self._hash(key, self.size)

    if self._table[index] is not None:
      for k, val in self._table[index]:
        if k == key: return val

    return None

  def __delitem__(self, key):
    val = self[key]
    if val is not None:
      index = self._hash(key, self.size)
      self._table[index].remove([key, val])
    return val
