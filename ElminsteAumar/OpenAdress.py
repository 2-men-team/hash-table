import math

class OpenAdress:
    def __init__(self, m, hash_fn):
        self.hash = [None for x in range(m)]
        self.m = m
        self.collision_num = 0
        self.hash_fn = hash_fn

    def collisions(self):
        return self.collision_num

    def insert(self, data):
        count = 0
        key = self.hash_func(data, count)
        if self.hash[key] is not None:
            self.collision_num += 1
        while self.hash[key] is not None and count < self.m:
            key = self.hash_func(data, count)
            count += 1
        self.hash[key] = data

    def get(self, data): # return index of data element
        count = 0
        key = self.hash_func(data)
        while self.hash[key] != data and count < self.m:
            key = self.hash_func(data, count)
            count += 1
        return key

    def hash_func(self, data, i):
        return self.hash_fn(data, self.m, i)

    def help_hash_1(self, data):
        return (data % self.m)

    def help_hash_2(self, data):
        return int(math.floor(((data*(2654435761/float(2**32))) % 1)*self.m))

    def include(self, data):
        count = 0
        key = self.hash_func(data, count)
        while self.hash[key] != data and self.hash[key] is not None and count < self.m:
            count += 1
            key = self.hash_func(data, count)
        if self.hash[key] is None:
            return False
        return True
