import sys
import math

file_in = sys.argv[1]
file_out = sys.argv[2]
k = int(sys.argv[3])

def parse(file_in):
    with open(file_in) as file:
        parsed = file.read().split("\n")
        parsed[0] = parsed[0].split(" ")
        if parsed[-1] == '':
            del parsed[-1]
        N = int(parsed[0][0])
        arr = parsed[1:N+1]
        sums = parsed[N+1:]
    return [int(x) for x in arr], [int(x) for x in sums]

def output(file_out, args):
    with open(file_out, "a") as file:
        for arg in args:
            file.write(str(arg) + " ")
        file.write("\n")

def force(file_in, file_out):
    array, sums = parse(file_in)
    for S in sums:
        found = False
        for i in array:
            if found == True:
                break
            for j in array:
                if(i + j == S):
                    found = True
                    print(S, i, j)
                    break

def main(file_in, file_out, k):
    array, sums = parse(file_in)
    if k == 1 or k == 2:
        table = Hashtable(len(array), k)
    if k == 3 or k == 4 or k == 5:
        table = OpenAdress(len(array), k)

    for elem in array:
        table.insert(elem)
    output(file_out, [table.collisions()])

    for S in sums:
        print(S)
        found = False
        for elem in array:
            if(table.include(S-elem)):
                found = True; break
        if(found):
            output(file_out, [elem, S-elem])
        else:
            output(file_out, [0, 0])

# linked list implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = temp

    def insert_start(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def length(self):
        current = self.head
        length = 0
        while current is not None:
            length += 1
            current = current.next
        return length

    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return current
            else:
                current = current.next
        return None

    def delete(self, data):
        current = self.head
        prev = None
        while current is not None:
            if current.data == data:
                break
            else:
                prev = current
                current = current.next
        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next

    # unnecessary
    def include(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            else:
                current = current.next
        return False

class Hashtable:
    def __init__(self, length, k):
        self.hash = [Linked_list() for x in range(3*length)]
        self.m = 3*length
        self.k = k

    def collisions(self):
        collisions = 0
        for llist in self.hash:
            if llist.head is not None:
                collisions += llist.length() - 1
        return collisions

    def hash_func(self, data):
        if self.k == 1:
            return (data % (self.m))
        elif self.k == 2:
            return int(math.floor(((data*(2654435761/float(2**32))) % 1)*self.m))

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

class OpenAdress:
    def __init__(self, length, k):
        self.hash = [None for x in range(3*length)]
        self.m = 3*length
        self.k = k
        self.collision_num = 0

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
        key = self.hash_func(data)
        count = 1
        while self.hash[key] != data and count < self.m:
            key = self.hash_func(data, count)
            count += 1
        return key

    def hash_func(self, data, i):
        if self.k == 3:
            return (self.help_hash_1(data) + i) % self.m
        if self.k == 4:
            return (self.help_hash_1(data) + i + i**2) % self.m
        if self.k == 5:
            return (self.help_hash_1(data) + i*self.help_hash_2(data)) % self.m

    def help_hash_1(self, data):
        return (data % self.m)

    def help_hash_2(self, data):
        return int(math.floor(((data*(2654435761/float(2**32))) % 1)*self.m))

    def include(self, data):
        count = 0
        key = self.hash_func(data, count)
        while self.hash[key] != data and count < self.m:
            key = self.hash_func(data, count)
            count += 1
        if count == self.m:
            return False
        return True

# running
main(file_in, file_out, k)
#force(file_in, file_out)
