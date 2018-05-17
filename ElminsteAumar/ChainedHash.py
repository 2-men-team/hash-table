from Llist import Linked_list

class ChainedHash:
    def __init__(self, m, hash_fn):
        self.hash = [Linked_list() for x in range(m)]
        self.m = m
        self.hash_fn = hash_fn

    def collisions(self):
        collisions = 0
        for llist in self.hash:
            if llist.head is not None:
                collisions += llist.length() - 1
        return collisions

    def hash_func(self, data):
        return self.hash_fn(data, self.m)

    def search(self, data):
        key = self.hash_func(data)
        found = self.hash[key].search(data)
        return found

    def insert(self, data):
        key = self.hash_func(data)
        self.hash[key].insert_start(data)

    def delete(self, data):
        key = self.hash_func(data)
        self.hash[key].delete(data)

    def length(self):
        return len(self.hash)

    def include(self, data):
        key = self.hash_func(data)
        return self.hash[key].include(data)
