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

    def include(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            else:
                current = current.next
        return False
