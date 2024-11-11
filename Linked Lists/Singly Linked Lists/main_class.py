class Node:

    def __init__(self, info, next=None):
        self.info = info
        self.next = next

    def get_info(self):
        return self.info

    def set_info(self, value):
        self.info = value

    def get_next(self):
        return self.next

    def set_next(self, ptr):
        self.next = ptr

    def __str__(self):
        return str(self.info)


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.head is None

    def traversal(self):
        if self.is_empty():
            return "Empty List!!!"
        current = self.head
        while current:
            print(current.get_info(),end=" ==> ")
            current = current.next

    def search_node(self, value):
        if self.is_empty():
            return "Empty List!!!"
        current = self.head
        found = False
        while (found is False) and (current is not None):
            if current.info == value:
                found = True
                return current
            else:
                current = current.next
        return current

    def insert_first(self, new: Node):
        if self.head is None:
            self.head = new
        else:
            new.next = self.head
            self.head = new

    def insert_after_node(self, new: Node, old: Node):
        if self.is_empty():
            self.head = new
        else:
            current = self.head
            while current:
                if current.info == old.info:
                    new.next = current.next
                    current.next = new
                    return True
                current = current.next

    def insert_end(self, node):
        pass


    def delete_node(self, info):
        pass

