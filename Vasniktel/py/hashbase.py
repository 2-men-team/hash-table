class HashBase(object):
  def __init__(self, size, hashFunc):
    self.size = size
    self._table = [None] * self.size
    self._hash = hashFunc
    self.collisions = 0

  def __setitem__(self, key, value):
    pass

  def __getitem__(self, key):
    pass

  def __contains__(self, key):
    return self[key] is not None

  def __delitem__(self, key):
    pass
