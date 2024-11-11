class Node:

    def __init__(self, info, next=None, prev=None):
        self.info = info
        self.next = next
        self.prev = prev

    def get_info(self):
        return self.info

    def set_info(self, value):
        self.info = value

    def get_next(self):
        return self.next

    def set_next(self, ptr):
        self.next = ptr

    def get_prev(self):
        return self.prev

    def set_prev(self, ptr):
        self.prev = ptr

    def __str__(self):
        return str(self.info)
