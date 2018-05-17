def divHash(key, size):
  return hash(key) % size

def multHash(key, size):
  golden = (1 + 5 ** 0.5) / 2
  return int(( (hash(key) * (golden - 1)) % 1 ) * size)

def linearHash(key, size, i):
  return (multHash(key, size) + i) % size

def quadHash(key, size, i):
  return (multHash(key, size) + i + i ** 2) % size

def doubleHash(key, size, i):
  return (divHash(key, size) + i * multHash(key, size)) % size

hashes = {
  'divide': divHash,
  'multiply': multHash,
  'linear': linearHash,
  'quadratic': quadHash,
  'double': doubleHash
}
